from flask import Flask
from session.session import Session
from utils import ml, functions
from models.tweet import Tweet


app = Flask(__name__)

session = Session(
    url="https://api.twitter.com/2/"
)


@app.route('/tweets/sentiment/<user_id>', methods=['GET'])
def get_sentiment(user_id: str):
    response = session.get(
        endpoint=f"/users/{user_id}/tweets",
        params={"screen_name": user_id}
    )
    if not response.ok:
        return functions.handle_error_response(response)
    sentiment = ml.predict_sentiment(tweets=[Tweet.from_json(tweet_data).text for tweet_data in response.json()])
    return {"status_code": 200, "sentiment": sentiment}, 200


@app.route('/tweets/freq_langs', methods=['GET'])
def get_freq_langs():
    query = {'query': '#programming', 'max_results': 1000}
    response = session.get(
        endpoint="tweets/search/recent",
        params=query
    )
    if not response.ok:
        return functions.handle_error_response(response), response.status_code
    response_json = response.json()
    tweets = [Tweet.from_json(tweet_json) for tweet_json in response_json.get("data")]
    programming_langs_histogram = functions.count_programming_languages(tweets)
    return programming_langs_histogram, 200


@app.route('/tweets/most_popular/<user_id>', methods=['GET'])
def get_user_most_liked_tweets(user_id: str):
    params = {"tweet.fields": "public_metrics.like_count"}
    response = session.get(
        endpoint=f"/users/{user_id}/tweets",
        params=params
    )
    if not response.ok:
        return functions.handle_error_response(response), response.status_code
    sorted_by_popularity = functions.sort_by_likes([Tweet.from_json(data) for data in response.json().get("data")])
    response = {"status_code": 200, "tweets_sorted": []}

    for tweet in sorted_by_popularity:
        response["tweets_sorted"].append(str(tweet))
    return response, 200


if __name__ == "__main__":
    app.run(debug=True)
