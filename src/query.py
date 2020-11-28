import nltk 
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
import math

from index import buildIndex

stemmer = SnowballStemmer('spanish')

def preprocessingQuery(inputText):
    inputText = inputText.lower()
    inputText = nltk.word_tokenize(inputText)

    result = []

    for i in inputText:
        result.append(stemmer.stem(i))

    return result

def tf_idf(tf, df, totalTweets):
    return math.log(1 + tf, 10) * math.log(totalTweets / df, 10)

def getTfIdfInput(query, invertedIndex, totalTweets):
    result = {}

    for word in query:
        if word in invertedIndex:
            df = invertedIndex[word][0]
            tfIdf = tf_idf(1, df, totalTweets)
            result[word] = tfIdf

    return result

def getSqrtInput(tfIdf):
    total = 0

    for word in tfIdf:
        total += tfIdf[word] ** 2

    return (total ** 0.5)

def getTfIdfIndex(query, invertedIndex, totalTweets):
    result = {}

    for word in query:
        for dataId in invertedIndex[word][1]:
            tf = invertedIndex[word][1][dataId]
            df = invertedIndex[word][0]
            tfIdf = tf_idf(tf, df, totalTweets)
            # {tweetId: {word: tfIdf}}

            if dataId not in result:
                result[dataId] = {}

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


def query(inputText, k, invertedIndex, totalTweets):
    inputText = preprocessingQuery(inputText)
    tfIdfInput = getTfIdfInput(inputText, invertedIndex, totalTweets)
    tfIdfIndex = getTfIdfIndex(inputText, invertedIndex, totalTweets)
    cos = cosScore(tfIdfInput, tfIdfIndex)

    dict_items = cos.items()

    if k < len(cos):
        kElem = list(dict_items)[:k]
        return kElem
    else:
        kElem = list(dict_items)[:]
        return kElem
