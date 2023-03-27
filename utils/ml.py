from textblob import TextBlob
from models.tweet import Tweet


def predict_sentiment(tweets: list[Tweet]) -> str:

    total_sentiment = 0
    for tweet in tweets:
        blob = TextBlob(tweet.text)
        sentiment = blob.sentiment.polarity
        total_sentiment += sentiment

    avg_sentiment = total_sentiment / len(tweets)

    if avg_sentiment > 0:
        return "POSITIVE"
    elif avg_sentiment < 0:
        return "NEGATIVE"
    else:
        return "NEUTRAL"
