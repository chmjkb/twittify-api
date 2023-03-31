import json


class Tweet:
    def __init__(self, user: str, text: str, created_at: str, likes: int, reposts_count: int):
        self._user = user
        self._text = text
        self._created_at = created_at
        self._likes = likes
        self._reposts_count = reposts_count

    @classmethod
    def from_json(cls, json_obj: dict):
        tweet = cls(
            user=json_obj.get("user", {}),
            text=json_obj.get("text", {}),
            created_at=json_obj.get("created_at", {}),
            likes=json_obj.get("public_metrics", {}).get("likes_count", "Not specified"),
            reposts_count=len(json_obj.get("public_metrics", {}).get("reposts_count", "Not specified"))
        )
        return tweet

    @property
    def user(self) -> str:
        return self._user

    @property
    def text(self) -> str:
        return self._text

    @property
    def created_at(self) -> str:
        return self._created_at

    @property
    def json(self) -> dict:
        data = {
            "user": self._user,
            "text": self._text,
            "created_at": self._created_at,
            "likes_count": self._likes,
            "reposts_count": self._reposts_count
        }
        return data

    def __str__(self) -> str:
        return str(self.json)

