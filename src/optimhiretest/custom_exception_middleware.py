import datetime
import json
import traceback

from django.http import HttpResponse


class CustomViewException(Exception):
    def __init__(self, value, http_code=500):
        self.value = value
        self.http_code = http_code

    def __str__(self):
        return repr(self.value)


class CustomExceptionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response

    def process_exception(self, request, exception):
        """
        Custom exception processing
        :param request: is request
        :param exception: is exception to be handled
        :return: HttpResponse to the client
        """

        print(traceback.format_exc())
        exception_message = exception.value if isinstance(exception, CustomViewException) else exception.args[0]
        print(exception_message)
        response = {
            'data': {},
            'timestamp': str(datetime.datetime.now()),
            'error': f'{exception_message}'
        }
        return HttpResponse(json.dumps(response), content_type="application/json", status=exception.http_code)
