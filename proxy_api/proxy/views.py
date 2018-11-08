import urllib.request
import urllib.error

from django.http import HttpResponse

from django.shortcuts import get_object_or_404
from django.utils.http import urlencode

from proxy_api.proxy.models import API, APICallLog


def _extract_headers(request):
    def convert_header_name(s):
        s = s.replace('HTTP_', '', 1)
        s = s.replace('_', '-')
        return s

    headers = dict((convert_header_name(name), value)
                   for name, value
                   in request.META.items() if name.startswith('HTTP_'))
    del headers['HOST']
    del headers['ACCEPT-ENCODING']

    if 'CONTENT_TYPE' in request.META:
        headers['CONTENT-TYPE'] = request.META['CONTENT_TYPE']

    if 'CONTENT_LENGTH' in request.META:
        headers['CONTENT-LENGTH'] = request.META['CONTENT_LENGTH']

    if 'proxy_accepted_content_type' in request.GET:
        headers['ACCEPT'] = request.GET['proxy_accepted_content_type']
        del request.GET['proxy_accepted_content_type']

    return headers


def _create_request(api, api_path, request):
    headers = _extract_headers(request)

    url = api.url + "/" + api_path
    if request.GET:
        url += '?' + urlencode(request.GET)

    return urllib.request.Request(url, data=request.body, headers=headers,
                                  method=request.method)


def forward(request, api_slug, api_path=""):
    api = get_object_or_404(API, slug=api_slug)

    if not api.methods.filter(name=request.method).exists():
        return HttpResponse(
            "Method {} for API '{}' is not allowed".format(
                request.method, api_slug), status=405)

    response_kwargs = {}
    try:
        response = urllib.request.urlopen(_create_request(
            api, api_path, request))
        response_kwargs['content'] = response.read()
        response_kwargs['status'] = response.getcode()
        response_kwargs['reason'] = response.reason
        response_kwargs['charset'] = response.info().get_content_charset()
        response_kwargs['content_type'] = response.headers['content-type']
    except urllib.error.HTTPError as err:
        response_kwargs['content'] = err.read()
        response_kwargs['status'] = err.code
        response_kwargs['reason'] = err.reason

    APICallLog.objects.create(api=api, request_body=request.body,
                              request_headers={name: repr(value)
                                               for name, value
                                               in request.META.items()},
                              **response_kwargs)
    return HttpResponse(**response_kwargs)
