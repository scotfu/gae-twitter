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
#from .models import Tweet
from .utils import *

@app.route('/',methods=['GET','POST'])
def index():
    if request.method=='GET':
        return render_template('index.html')

@app.route('/action/',methods=['GET','POST'])
def action():
    if request.method == 'POST':
        location=request.form['location']
        key_word=request.form['key_word']
        tweets = search(key_word,location)    
        word_dict=count_word(tweets)
        top_ten=get_top_ten(tweets,word_dict)
        ''' 
for tweet in top_ten:
            t=Tweet()
            t.text=tweet['text']
            t.from_user=tweet['from_user']
            t.from_user_name=tweet['from_user_name']
            t.created_at=tweet['created_at']
            t.location=tweet['geo']
            t.key_word=key_word
            t.weight=tweet['quan']
            t.image=tweet['profile_image_url']
            t.put()
        q=Tweet.all()    
        q.filter('key_word=',key_word)
        q.order('-weight')
        ''' 
        return result(tweets=top_ten,key_word=key_word)
    return '?'
@app.route('/result')
def result(tweets,key_word):
    if tweets:
        print key_word
        return render_template('result.html',tweets=tweets,key_word=key_word)
    else:
        return redirect(url_for('index'))
