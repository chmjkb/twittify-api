from typing import Optional
from collections import defaultdict
from models.tweet import Tweet
from re import findall
from enums import ErrorType
import requests


def count_programming_languages(tweets: list[Tweet], programming_languages: Optional[list[str]] = None) -> dict:
    """
    Given a list of tweet objects, returns number of occurrences of each passed or previously defined programming
    languages in that list of tweets
    :param tweets: List of objects representing a Tweet
    :param programming_languages: Optional list of programming languages to search for in the tweets
    :return: Dictionary with key-value pairs of language: number of occurrences in the tweets
    """
    if programming_languages is None:
        programming_languages = ['Python', 'JavaScript', 'Java', 'Ruby', 'R', 'Rust', 'C++', 'C#']

    language_counts = defaultdict(int)
    for tweet in tweets:
        text = tweet.text.lower()
        for language in programming_languages:
            matches = findall(fr'\W({language.lower()})\W', text)
            language_counts[language] += len(matches)
    return dict(language_counts)


def handle_error_response(response: requests.Response):
    return ErrorType.get_error_from_code(response.status_code)