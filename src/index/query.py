import nltk 
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
import math

import preprocessing
import index
from index import buildIndex

stemmer = SnowballStemmer('spanish')
[invertedIndex, totalTweets] = buildIndex()

def preprocessingQuery(inputText):
    inputText = inputText.lower()
    inputText = nltk.word_tokenize(inputText)
    result = stemmer.stem(inputText)

    return result

def tf_idf(tf, df):
    return math.log(1 + tf, 10) * math.log(totalTweets / df, 10)

def getTfIdfInput(query, isInput):
    result = {}

    for word in query:
        if word in invertedIndex:
            df = invertedIndex[term][0]
            tfIdf = tf_idf(1, df)
            result[word] = tfIdf

    return result

def getSqrtInput(tfIdf):
    total = 0

    for word in tfIdf:
        total += tfIdf[word] ** 2

    return (total ** 0.5)

def getTfIdfIndex(query):
    result = {}

    for word in query:
        for dataId in invertedIndex[word][1]:
            tf = invertedIndex[word][1][dataId]
            df = invertedIndex[word][0]
            tfIdf = tf_idf(tf, df)
            # {tweetId: {word: tfIdf}}
            result[dataId][word] = tfIdf

    return result

def getSqrtIndex(tfIdf):
    result = {}

    for dataId in tfIdf:
        total = 0
        for word in tfIdf[dataId]:
            total += tfIdf[dataId][word] ** 2

        result[dataId] = (total ** 0.5)

    return result

def cosScore(tfIdfInput, tfIdfIndex):
    sqrtInput = getSqrtInput(tfIdfInput)
    sqrtIndex = getSqrtIndex(tfIdfIndex)

    score = {}

    for dataId in tfIdfIndex:
        product = 0
        sqrtTotal = sqrtInput * sqrtIndex[dataId]
        for word in tfIdfIndex[dataId]:
            product += tfIdfIndex[dataId][word] * tfIdfInput[word]

        score[dataId] = product / sqrtTotal

    score = {k: v for k, v in sorted(score.items(), key=lambda item: item[1])}

    return score


def query(inputText, k):
    inputText = preprocessingQuery(inputText)
    tfIdfInput = getTfIdfInput(inputText)
    tfIdfIndex = getTfIdfIndex(inputText)
    cos = cosScore(tfIdfInput, tfIdfIndex)

    if k < len(cos):
        return cos[ : k]
    else:
        return cos
