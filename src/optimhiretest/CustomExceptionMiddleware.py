import json
import traceback

from django.http import HttpResponse


class CustomViewException(Exception):
    def __init__(self, value):
        self.value = value

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

        print(traceback.format_exc())
        exception_message = exception.value if isinstance(exception, CustomViewException) else exception.args[0]
        print(exception_message)
        error_obj = {
            'error': f'{exception_message}'
        }
        # TODO: create 'errors list' to identify and parse 'error-keywords' to specific error objects to be sent in response
        return HttpResponse(json.dumps(error_obj), content_type="application/json", status=500)
