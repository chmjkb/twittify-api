from typing import Optional
import requests
from config.conf import Config


class Session:
    """
    A wrapper class for requests. The need for this class is dictated by the requirement of OAuth2.

    :param url: The base URL for the API endpoint.
    """
    def __init__(self, url: str):
        self._url = url
        self._session = requests.Session()
        self._session.headers.update({"Authorization": f"Bearer {Config.token}"})

    def get(self, endpoint: str, params: Optional[dict] = None, headers: Optional[dict] = None) -> requests.Response:
        """
        Simple mechanism to send GET requests to a certain endpoint
        :param endpoint: A specific endpoint of twitter API, i.e /tweets/
        :param params: Params for the API request
        :param headers: Headers for the API request
        :return: requests.Response object
        """
        response = self._session.get(
            url=self._url + endpoint,
            params=params,
            headers=headers
        )
        return response

    def post(self, endpoint: str, params: Optional[dict] = None, headers: Optional[dict] = None) -> requests.Response:
        """
        Simple mechanism to send POST requests to a certain endpoint
        :param endpoint: A specific endpoint of twitter API, i.e /tweets/
        :param params: Params for the API request
        :param headers: Headers for the API request
        :return: requests.Response object
        """
        response = self._session.post(
            url=self._url + endpoint,
            params=params,
            headers=headers
        )
        return response
