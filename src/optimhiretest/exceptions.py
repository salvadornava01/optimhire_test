from rest_framework.exceptions import APIException, _get_error_details
from rest_framework.status import HTTP_400_BAD_REQUEST


class QueryParamException(APIException):
    status_code = HTTP_400_BAD_REQUEST
    default_detail = 'Query param should be defined'


class BadBodyRequestException(APIException):
    def __init__(self, detail=None, code=None):
        if detail is None:
            detail = self.default_detail
        if code is None:
            code = self.default_code

        self.detail = ','.join([f'field {field} error: {detail[field][0]}' for field in detail])
    status_code = HTTP_400_BAD_REQUEST
    default_detail = 'Body request is not correct'