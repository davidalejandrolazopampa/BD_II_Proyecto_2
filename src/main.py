from flask import Flask,render_template, request, session, Response, redirect
from query import query
from index import buildIndex

indexPath = '../files/invertedIndex.json'
dataPath = '../example/'

app = Flask(__name__)

[invertedIndex, totalTweets, allTweets] = buildIndex(indexPath, dataPath)

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/retrieval")
def retrieval():
    textInput = request.args.get("query")
    k = request.args.get("range")
    retrievalResult = {}

    tweets = query(textInput, int(k), invertedIndex, totalTweets)
    for tweet in tweets:
        retrievalResult[tweet[0]] = allTweets[int(tweet[0])]

    return render_template("retrieval.html", tweets = retrievalResult)

if __name__ == "__main__":
    app.secret_key = ".."
    app.run(port=5000, threaded=True, host=('127.0.0.1'))
