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
        return json.dumps(tweets)
