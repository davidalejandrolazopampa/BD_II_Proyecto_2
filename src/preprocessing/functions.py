import nltk 
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
import itertools
import collections
from collections import Counter

def getStopWords():
    stopFile = open("../files/stoplist.txt", "r")
    stopWords = []

    for line in stopFile:
        stopWords = stopWords.append(line)

    stopWords += ['?', '.',',', ';', '«', ':', '¿', '!', '¡', '<', '>', '😆']

    return stopWords


