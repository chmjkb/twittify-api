class ErrorType:
    """
    Class responsible for returning a proper error code
    """
    def __init__(self):
        self._error_types = {
            "404": "Resource not found",
            "500": "Internal server error",
            "401": "Unauthorized,please check whether your bearer token is still valid or provide"
                   "TWITTER_BEARER_TOKEN env variable if you haven't done so."
        }

    @staticmethod
    def get_error_from_code(code: int) -> str:
        return ErrorType()._error_types.get(str(code))
