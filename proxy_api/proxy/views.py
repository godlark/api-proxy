import urllib.request
import urllib.error

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from django.shortcuts import get_object_or_404

from proxy_api.core.utils import extract_headers, get_response_data_for_request, \
    get_path
from proxy_api.proxy.models import API, APICallLog


def _extract_headers(request):
    headers = extract_headers(request.META)

    if 'proxy_accepted_content_type' in request.GET:
        headers['ACCEPT'] = request.GET['proxy_accepted_content_type']
        del request.GET['proxy_accepted_content_type']

    return headers


@login_required(login_url='/admin')
def forward(request, api_slug, api_path=""):
    api = get_object_or_404(API, slug=api_slug)

    if not api.methods.filter(name=request.method).exists():
        return HttpResponse(
            "Method {} for API '{}' is not allowed".format(
                request.method, api_slug), status=405)

    path = get_path(api_path, request)
    proxy_headers = _extract_headers(request)
    proxy_request = urllib.request.Request(
        api.url + "/" + path, data=request.body, headers=proxy_headers,
        method=request.method)

    response_kwargs = get_response_data_for_request(proxy_request)

    APICallLog.objects.create(api=api, request_path=path,
                              request_body=request.body,
                              request_body_binary=request.body,
                              request_headers={name: str(value)
                                               for name, value
                                               in request.META.items()},
                              **response_kwargs)
    return HttpResponse(**response_kwargs)
