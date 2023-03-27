from flask import Flask, request
from session import Session
from utils import ml, functions
from error_handler import handle_error_response
from models.tweet import Tweet


app = Flask(__name__)

session = Session(
    url="https://api.twitter.com/2/"
)


@app.route('/tweets/sentiment/<username>', methods=['GET'])
def get_sentiment(username: str):
    from_date = request.args.get("from")
    response = session.get(
        endpoint="statuses/user_timeline.json",
        params={"screen_name": username, "from": from_date}  # TODO -> from parameter is not going to work
    )
    if not response.ok:
        return handle_error_response(response)
    sentiment = ml.predict_sentiment(tweets=[tweet.text for tweet in response.json()])
    return {"sentiment": sentiment}, 200


@app.route('/tweets/freq_langs', methods=['GET'])
def get_programming_langs():
    query = {'query': '#programming', 'max_results': 1000}
    response = session.get(
        endpoint="tweets/search/recent",
        params=query
    )
    if not response.ok:
        return {"error_message": f"Twitter API returned: {response.reason}"}, response.status_code
    response_json = response.json()
    tweets = [Tweet.from_json(tweet_json) for tweet_json in response_json.get("data")]
    if not tweets:
        return {"error_message": f"No content, invalid programming langs?"}, 204
    programming_langs_histogram = functions.count_programming_languages(tweets)
    return programming_langs_histogram, 200


# @app.route('/tweets/most_popular/<user_id>', methods=['GET'])
# def get_user_most_popular_tweets(user_id: str):
#     pass


# TODO -> Post a random, AI generated tweet?

if __name__ == "__main__":
    app.run(debug=True)
