import os
from utils.exceptions import TokenNotFoundException


class Config:
    def __init__(self):
        self._token = self._get_key("TWITTER_BEARER_TOKEN")

    @staticmethod
    def _get_key(key):
        value = os.environ.get(key)
        if value is None:
            raise TokenNotFoundException(message=f"{key} is not found in environment variables!")
        return value

    @property
    def token(self):
        return self._token
