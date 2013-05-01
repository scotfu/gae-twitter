# /usr/env python
#-*- coding:utf8 -*-
import urllib2
import json
import urllib
import pprint
import re
import pdb
import sys
import os

reload(sys)
sys.setdefaultencoding('utf-8')

DIR=os.path.dirname(__file__).replace('\\', '/')

MAP_URL='http://maps.googleapis.com/maps/api/geocode/json?'
TWITTER_URL='http://search.twitter.com/search.json?'

 
# AFINN-111 is as of June 2011 the most recent version of AFINN
filenameAFINN = DIR+'/AFINN/AFINN-111.txt'
afinn = dict(map(lambda (w, s): (w, int(s)), [ws.strip().split('\t') for ws in open(filenameAFINN) ]))
 
# Word splitter pattern
pattern_split = re.compile(r"\W+")
 
def sentiment(text):
    """
    Returns a float for sentiment strength based on the input text.
    Positive values are positive valence, negative value are negative valence. 
    """
    words = pattern_split.split(text.lower())
    sentiments = map(lambda word: afinn.get(word, 0), words)
    if sentiments:
        # How should you weight the individual word sentiments? 
        # You could do N, sqrt(N) or 1 for example. Here I use sqrt(N)
        sentiment = float(sum(sentiments))/(len(sentiments))
        
    else:
        sentiment = 0
    return sentiment
 
def search(key_word,location):
    parameters = {'address':location,'sensor':'false'}
    parameters = urllib.urlencode(parameters)
    geocode = urllib2.urlopen(MAP_URL+parameters).read()
    data = json.loads(geocode)
    lat = data['results'][0]['geometry']['location']['lat']
    lng = data['results'][0]['geometry']['location']['lng']
    parameters = {'q':str(key_word),'geocode':','.join([str(lat),str(lng),'10mi']), 'result_type':'mixed','rpp':'1000'}
    parameters = urllib.urlencode(parameters)
    tweets= json.loads(urllib2.urlopen(TWITTER_URL+parameters).read())['results']
    return tweets

def count_word(tweets):
    word_dict={}
    for tweet in tweets:
        for word in pattern_split.split(tweet['text'].lower()):
            try:
                word_dict[word]+=1
            except:
                word_dict[word]=1
#    del word_dict[""]
    return word_dict


def get_top_ten(tweets,word_dict):
    for tweet in tweets:
        tweet['quan']=0
        for word in tweet['text'].lower().split():
            tweet['quan']+=word_dict.get(word,0)
        tweet['quan']=tweet['quan']/len(tweet['text'].lower().split())
        
    tweets.sort(key=lambda tweet: tweet['quan'],reverse=True)
    return tweets[:10]

if __name__ =='__main__':
    tweets=search('sports','NEW York')
    pprint.pprint([tweet.get('quan') for tweet in get_top_ten(tweets,count_word(tweets))])
    
