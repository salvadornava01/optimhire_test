from src.optimhiretest.custom_exception_middleware import CustomViewException


def get_query_param_or_bad_request(param_name, request_query_params):
    if param_name not in request_query_params:
        raise CustomViewException(f'Query param: {param_name} should be defined', 500)
    return request_query_params[param_name]