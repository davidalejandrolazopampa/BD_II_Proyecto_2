import os
import json
import nltk 
from os import path
from nltk.stem import SnowballStemmer

import preprocessing

stemmer = SnowballStemmer('spanish')

DATA_PATH = '../../example/'
INDEX_PATH = '../files/invertedIndex.json'

def read(path):
    indexFile = open(path, 'r')
    invertedIndex = json.load(indexFile)
    indexFile.close()

    return invertedIndex

def write(path, invertedIndex):
    indexFile = open(path, 'w')
    json.dump(indexDB, indexFile)
    indexFile.close()


def generateInvertedIndex():
    processedWords = preprocessing(DATA_PATH)

    dataList = os.listdir(DATA_PATH)

    invertedIndex = {}
    totalTweets = 0

    for word in processedWords:
        invertedIndex[word] = [0, {}] # df, {id: tf}

    for dataFile in dataList:
        data = open(dataPath + dataFile, 'r')
        tweets = json.load(data)

        for tweet in tweets:
            if tweet['retweeted'] is False:
                dataId = tweet['id']
                text = tweet['text'].lower()

                text = nltk.word_tokenize(text)

                for word in text:
                    temp = stemmer.stem(word)

                    if temp in processedWords:
                        if dataId not in invertedIndex[temp][1]:
                            invertedIndex[temp][0] += 1
                            invertedIndex[temp][1][dataId] = 1
                        else:
                            invertedIndex[temp][1][dataId] += 1
            totalTweets++

        data.close()

    return [invertedIndex, totalTweets]

def buildIndex():
    if path.exists(INDEX_PATH):
        invertedIndex = read(INDEX_PATH)
    else:
        invertedIndex = generateInvertedIndex()
        write(INDEX_PATH, invertedIndex)

    return invertedIndex

