'''
Created on Feb 1, 2017

@author: Zhongchao
'''

# Import the necessary package to process data in JSON format
try:
    import json
except ImportError:
    import simplejson as json
from twitter import parse_tweet
import string
import csv

def first_match(stext):
    for i in stext:
        if i in emoji:
            return i
    return 

def rev_find(text, start_idx):
    flag = False
    i = start_idx - 1
    while (i >= 0):
        if ((text[i] in punc_set or text[i] == ' ') and not flag):
            i = i - 1
        elif (text[i] not in punc_set and  text[i] != ' ' and not flag):
            end = i
            flag = True
            i = i - 1
        elif (text[i] not in punc_set and flag):
            i = i - 1
        elif (text[i] in punc_set and flag):
            start = i
            break
        elif (i == 0):
            start = i
            break
    if (i == -1):
        start = 0
    text = text[start:end+1]
    if (text[0] == '@'):
        text = text.split(' ', 1)[1]
    elif (text[0] in punc_set):
        text = text[1:]
    return text

def concat(emo, text):
    global cnt, data
    print text, '\n' # content of the tweet
    cnt = cnt + 1
    tmp = {}
    tmp['text'] = text
    tmp['emoticon'] = emo
    data.append(tmp)
        
# We use the file saved from last step as example
tweets_filename = 'emoticons.txt'
tweets_file = open(tweets_filename, "r")
emoji = parse_tweet.Emoticons.POSITIVE + parse_tweet.Emoticons.NEGATIVE

threshold = 5
cnt = 0
punc_set = set([':', '.', '@', '!', '?', '#', '$', '&', '%', '*', ';', '"'])
data = []

for line in tweets_file:
    try:
        # Read in one line of the file, convert it into a json object 
        tweet = json.loads(line.strip())
        if 'text' in tweet: # only messages contains 'text' field is a tweet
            text = tweet['text'].encode('ascii','ignore') 
            if any(ext in text for ext in emoji):
                stext = text.split(' ')
                emo = first_match(stext)
                start_idx = text.find(emo)
                text = rev_find(text, start_idx-1)
                text = text.replace('\n', ' ').replace('\r', '')
                if (len(text) >= threshold):
                    concat(emo, text)
    except:
        # read in a line is not in JSON format (sometimes error occured)
        continue

keys = data[0].keys()
with open('data.csv','wb') as f:
    wr = csv.DictWriter(f, keys)
    wr.writeheader()
    wr.writerows(data)
            
print cnt

    