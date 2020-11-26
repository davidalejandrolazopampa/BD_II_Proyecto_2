import os
import re
import codecs
import json
from nltk.stem import SnowballStemmer

import nltk 
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
import itertools
import collections
from collections import Counter

from functions import getStopWords

global dataPath = '../../data/'

def preprocessing():
    dataList = os.listdir(dataPath)
    stopWords = getStopWords()

    for dataFile in dataList:
