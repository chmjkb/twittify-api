import requests


def handle_error_response(twitter_response: requests.Response) -> dict:
    """

    :param twitter_response: Response received from the twitter API
    :return: Dictionary with explaination on what happened during the twitter API call
    """
    if twitter_response.status_code == 401:
        return {
            "error_message": "Unauthorized error, please check whether your bearer token is still valid or "
                             "provide TWITTER_BEARER_TOKEN env variable if you haven't done so.",
            "status_code": 401
        }

    if twitter_response.status_code == 400:
        return {
            "error_message": "Asset not found, please check whether you provided a correct username or other asset"
                             "reference.",
            "status_code": 404
        }

    if twitter_response.status_code == 500:
        return {
            "error_message": "Internal server error.",
            "status_code": 500
        }