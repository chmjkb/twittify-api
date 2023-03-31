from typing import Optional
from collections import defaultdict
from models.tweet import Tweet
from re import findall
import requests
from utils.enums import ErrorType


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


def sort_by_likes(tweets: list[Tweet]):
    """
    A simple function that takes in a list of tweets, and returns
    :param tweets: A list of tweet objects
    :return: List of Tweet objects, sorted by popularity
    """
    sorted_tweets = sorted(tweets, key=lambda tweet: tweet.likes, reverse=True)
    return sorted_tweets


def handle_error_response(response: requests.Response) -> dict:
    message = ErrorType.get_error_from_code(response.status_code)
    server_response = {
        "status_code": response.status_code,
        "error_message": message
    }
    return server_response
