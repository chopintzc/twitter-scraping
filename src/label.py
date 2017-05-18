'''
Created on Feb 1, 2017

@author: Zhongchao
'''

import csv
from twitter import parse_tweet

pos = parse_tweet.Emoticons.POSITIVE
neg = parse_tweet.Emoticons.NEGATIVE

data = []

with open('data.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        tmp = {}
        tmp['emoticon'] = row['emoticon']
        tmp['text'] = row['text']
        if (row['emoticon'] in pos):
            tmp['label'] = 'positive'
        else:
            tmp['label'] = 'negative'
        data.append(tmp)
        
keys = data[0].keys()
with open('label-data.csv','wb') as fb:
    wr = csv.DictWriter(fb, keys)
    wr.writeheader()
    wr.writerows(data)