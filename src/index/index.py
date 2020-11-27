import os
import json
import nltk 
from os import path
from nltk.stem import SnowballStemmer

from preprocessing import preprocessing

stemmer = SnowballStemmer('spanish')

def readIndexFile(path):
    with open(path) as f:
        invertedIndex = json.load(f)
    # indexFile = open(path, 'r')
    # invertedIndex = json.load(indexFile)
    # indexFile.close()

    return invertedIndex

def writeIndexFile(path, invertedIndex):
    indexFile = open(path, 'w')
    json.dump(invertedIndex, indexFile)
    indexFile.close()


def generateInvertedIndex(dataPath):
    processedWords = preprocessing(dataPath)

    dataList = os.listdir(dataPath)

    invertedIndex = {}

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

        data.close()

    return invertedIndex

def getTotalTweets(dataPath):
    dataList = os.listdir(dataPath)

    totalTweets = 0

    for dataFile in dataList:
        data = open(dataPath + dataFile, 'r')
        tweets = json.load(data)

        for tweet in tweets:
            if tweet['retweeted'] is False:
                totalTweets += 1

        data.close()
    
    return totalTweets

def buildIndex():
    indexPath = '../files/invertedIndex.json'
    dataPath = '../../example/'
    if path.exists(indexPath) == True:
        invertedIndex = readIndexFile(indexPath)
    else:
        invertedIndex = generateInvertedIndex(dataPath)
        writeIndexFile(indexPath, invertedIndex)

    return [invertedIndex, getTotalTweets(dataPath)]
