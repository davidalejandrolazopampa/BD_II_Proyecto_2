from flask import Flask,render_template, request, session, Response, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/search", methods = ['GET'])
def searchFile():
    query = request.args.get("query")
    tweets = queryIndex(indice, query, numTotalTweets)
    return render_template("resultado.html", consulta=query, tweets=tweets)


@app.route("/search/<string:consulta>/<int:tweet_id>")
def searchTweet(consulta, tweet_id):
    consult_formated = consulta.lower()
    tweet = getTweet(str(tweet_id))
    return render_template("tweets.html", consulta=consulta, tweet_id = tweet_id, tweet = tweet)

if __name__ == "__main__":
    app.secret_key = ".."
    app.run(port=5000, threaded=True, host=('127.0.0.1'))
