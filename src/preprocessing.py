import os
import json
import nltk 
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer

stemmer = SnowballStemmer('spanish')

def getStopWords(stopListPath = '../files/stopList.txt'):
    stopFile = open(stopListPath, "r")
    stopWords = []

    for line in stopFile:
        stopWords.append(line)

    stopWords += ['(', ')', '=', '+', '-', '|', '#', 'x', '/', '@', '?', '.',',', ';', '«', ':', '¿', '!', '¡', '<', '>', '😆', '👍', '_', '...', '👍🏻', '🏡', '”', '“', 'de', 'es', 'un', 'a', '%']

    stopFile.close()

    return stopWords

def preprocessing(dataPath = '../data/'):
    dataList = os.listdir(dataPath)
    stopWords = getStopWords()

    result = []

    for dataFile in dataList:
        data = open(dataPath + dataFile, 'r')
        tweets = json.load(data)

        for tweet in tweets:
            if tweet['retweeted'] is False:
                text = tweet['text'].lower()

                text = nltk.word_tokenize(text)
                cleanText = []

                for word in text:
                    if word not in stopWords:
                        temp = stemmer.stem(word)
                        result.append(temp)

        data.close()

    return set(result)

# print(preprocessing('../../example/'))
