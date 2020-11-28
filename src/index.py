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

    return invertedIndex, allTweets

def getInfo(dataPath):
    dataList = os.listdir(dataPath)

    totalTweets = 0
    allTweets = {}

    for dataFile in dataList:
        data = open(dataPath + dataFile, 'r')
        tweets = json.load(data)

        for tweet in tweets:
            if tweet['retweeted'] is False:
                dataId = tweet['id']
                text = tweet['text'].lower()
                totalTweets += 1

                allTweets[dataId] = text

        data.close()
    
    return [totalTweets, allTweets]

def buildIndex(indexPath, dataPath):
    if path.exists(indexPath) == True:
        invertedIndex = readIndexFile(indexPath)
    else:
        
        invertedIndex = generateInvertedIndex(dataPath)
        writeIndexFile(indexPath, invertedIndex)

    info = getInfo(dataPath)
    return [invertedIndex, info[0], info[1]]
