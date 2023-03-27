from utils.enums import ErrorType


def handle_error_response(error_code: int) -> dict:
    """

    :param error_code: Error code returned from API
    :return: Dictionary with explaination on what happened during the twitter API call
    """
    return ErrorType(error_code)
