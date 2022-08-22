import datetime

from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK


class SuccessAPIResponse(Response):

    def __init__(self, data=None, headers=None, exception=False):

        super().__init__(None, status=HTTP_200_OK)

        self.data = {'data': data, 'timestamp': datetime.datetime.now()}
        self.exception = exception

        if headers:
            for name, value in headers.items():
                self[name] = value
