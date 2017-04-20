'''
Created on Feb 2, 2017

@author: Zhongchao
'''

import nltk
import string
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import traceback
import sys
import re
import pickle
import csv


def removeUnicode(text):
    printable = set(string.printable)
    if isinstance(text, list):
        for v in text:
            if len(v) > 25:
                text = filter(lambda x: x in printable, v)
                break
    else:
        text = filter(lambda x: x in printable, text)

    return text if not isinstance(text, list) else ''


def tokenize(text):
    data = removeUnicode(text)
    data = data.lower()

    return nltk.word_tokenize(data)


def removeStopWordsAndDigits(tokens):
    pattern = re.compile(r'\d+')
    return [w for w in tokens if not w in stopwords.words('english') if not pattern.search(w)]


def stemTokens(tokens, stemmer=None):
    if not stemmer:
        stemmer = PorterStemmer()

    stemmed = []
    for item in tokens:
        stemmed.append(stemmer.stem(item))
    return stemmed




if __name__ == '__main__':
    data = []
    with open('label-data.csv') as f:
        reader = csv.DictReader(f)
        remove_punctuation = re.compile('([^\w\s])')
        for row in reader:
            tmp = {}
            tmp['emoticon'] = row['emoticon']
            text = row['text']
            text = remove_punctuation.sub('',text)
            tmp['label'] = row['label']
            tokens = tokenize(text)
            tokens = removeStopWordsAndDigits(tokens)
            tokens = stemTokens(tokens)
            tmp['text'] = tokens
            data.append(tmp)

    keys = data[0].keys()
    with open('stemmed-data.csv','wb') as fb:
        wr = csv.DictWriter(fb, keys)
        wr.writeheader()
        wr.writerows(data)


