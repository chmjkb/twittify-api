import enum
import requests


class ErrorType(enum.Enum):
    UNAUTHORIZED = ("Unauthorized error, please check whether your bearer token is still valid or provide "
                    "TWITTER_BEARER_TOKEN env variable if you haven't done so.", 401)
    NOT_FOUND = ("Asset not found, please check whether you provided a correct username or other asset reference.", 404)
    INTERNAL_SERVER_ERROR = ("Internal server error.", 500)

    def __new__(cls, message, status_code):
        obj = object.__new__(cls)
        obj._value_ = status_code
        obj.message = message
        cls._member_map_[status_code] = obj
        cls._member_map_[str(status_code)] = obj
        return obj

    def __str__(self):
        return str(self.value)

    @classmethod
    def from_value(cls, value):
        if isinstance(value, str):
            return cls._member_map_[value]
        return cls._value2member_map_[value]

    @property
    def error_message(self):
        return self.value[0]

    @property
    def status_code(self):
        return self.value[1]
