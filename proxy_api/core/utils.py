import urllib.request
import urllib.error

from django.utils.http import urlencode


def get_path(api_path, request):
    path = api_path
    if request.GET:
        path += '?' + urlencode(request.GET)
    return path


def extract_headers(request_meta):
    def convert_header_name(s):
        s = s.replace('HTTP_', '', 1)
        s = s.replace('_', '-')
        return s

    headers = dict((convert_header_name(name), value)
                   for name, value
                   in request_meta.items() if name.startswith('HTTP_'))
    del headers['HOST']
    del headers['ACCEPT-ENCODING']

    if 'CONTENT_TYPE' in request_meta:
        headers['CONTENT-TYPE'] = request_meta['CONTENT_TYPE']

    if 'CONTENT_LENGTH' in request_meta:
        headers['CONTENT-LENGTH'] = request_meta['CONTENT_LENGTH']

    return headers


def get_response_data_for_request(request):
    response_kwargs = {}
    try:
        response = urllib.request.urlopen(request)
        response_kwargs['content'] = response.read()
        response_kwargs['status'] = response.getcode()
        response_kwargs['reason'] = response.reason
        response_kwargs['charset'] = response.info().get_content_charset()
        response_kwargs['content_type'] = response.headers['content-type']
    except urllib.error.HTTPError as err:
        response_kwargs['content'] = err.read()
        response_kwargs['status'] = err.code
        response_kwargs['reason'] = err.reason
    return response_kwargs
