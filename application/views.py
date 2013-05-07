#-*-coding:utf-8-*-
import os
import random
import urllib2
import json
import urllib
import pprint
import re
import pdb
import sys
from flask import Blueprint, render_template, request, redirect, url_for, session
from werkzeug import secure_filename
from flask import make_response
from flask import render_template
from . import app
from .models import Tweet,Search,HighHit,HittoTweet
from .utils import *



@app.route('/',methods=['GET','POST'])
def index():
    if request.method=='GET':
        return render_template('index.html')

@app.route('/action/',methods=['GET','POST'])
def action():
    q=Search.all()    
    if request.method == 'POST':
        location=request.form['location'].lower()
        key_word=request.form['key_word'].lower()
        q.filter('key_word',key_word)
        q.filter('location',location)
        if q.count():
            return result(q.get(),test_x=10000)
        s=Search()
        s.key_word=key_word
        s.location=location
        s.put()
        
        tweets = search(key_word,location)    
        word_dict=count_word(tweets)
        w=word_dict
#        print w
        n=0
        while n< 11:
            hit=HighHit()
            hit.word=w.popitem()[0]
            hit.search=s
            hit.put()
            n+=1
        top_ten=get_top_ten(tweets,word_dict)
        test_x=1
        for tweet in top_ten:
            t=Tweet()
            t.text=tweet['text']
            t.from_user=tweet['from_user']
            t.from_user_name=tweet['from_user_name']
            t.created_at=tweet['created_at']
            t.location=tweet['geo']
            t.weight=tweet['quan']
            t.image=tweet['profile_image_url']
            t.sentiment=sentiment(t.text)
            t.put()
            
            for hit in s.highhit_set.run():
                if hit.word in t.text.split():
                    relation=HittoTweet()
                    relation.tweet=t
                    relation.highhit=hit
                    relation.put()
                test_x+=1
#        q.filter('key_word',key_word)
#        q.order('-weight')
        return result(search=s,test_x=test_x)
    return '?'
@app.route('/result')
def result(search,test_x):
    p=search.highhit_set.run()
    if p:
        return render_template('result.html',h=p,test_x=test_x)
