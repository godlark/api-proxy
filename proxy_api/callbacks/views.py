import urllib.request
import urllib.error

from django.http import HttpResponse

from django.shortcuts import get_object_or_404

from proxy_api.callbacks.models import Callback, CallbackCallLog
from proxy_api.core.utils import extract_headers, get_response_data_for_request, \
    get_path


def _forward_request(callback, path, headers, body, method):
    callback_request = urllib.request.Request(
        callback.url + "/" + path, data=body,
        headers=headers, method=method)

    response_kwargs = get_response_data_for_request(callback_request)

    CallbackCallLog.objects.create(callback=callback,
                                   request_path=path,
                                   request_body=body,
                                   request_body_binary=body,
                                   request_headers={name: str(value)
                                                    for name, value
                                                    in headers.items()},
                                   **response_kwargs)
    return HttpResponse(**response_kwargs)


def forward(request, callback_slug, callback_path=""):
    callback = get_object_or_404(Callback, slug=callback_slug)

    if not callback.methods.filter(name=request.method).exists():
        return HttpResponse(
            "Method {} for API '{}' is not allowed".format(
                request.method, callback_slug), status=405)

    path = get_path(callback_path, request)
    callback_headers = extract_headers(request.META)

    return _forward_request(callback, path, callback_headers,
                            request.body, request.method)


def replay(request, id):
    callback_call_log = get_object_or_404(CallbackCallLog, id=id)
    callback = callback_call_log.callback

    callback_path = callback_call_log.request_path
    callback_headers = extract_headers(callback_call_log.request_headers)
    callback_method = callback_call_log.request_headers['REQUEST_METHOD']
    callback_body = bytes(callback_call_log.request_body_binary)

    return _forward_request(callback, callback_path, callback_headers,
                            callback_body, callback_method)

