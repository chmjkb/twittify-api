from typing import Optional
from models.tweet import Tweet


def count_programming_languages(tweets: list[Tweet], programming_languages: Optional[list[str]] = None) -> dict:
    """

    :param tweets: List of objects representing a Tweet
    :param programming_languages:
    :return: Dictionary with key-value pairs of language: number of occurences in the tweets
    """
    result = {}
    if programming_languages is None:
        programming_languages = ['Python', 'JavaScript', 'Java', 'Ruby', 'R', 'Rust', 'C++', 'C#']
    for tweet in tweets:
        print(tweet.text)


