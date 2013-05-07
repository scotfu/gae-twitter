# /usr/env python
#-*- coding:utf8 -*-

from google.appengine.ext import db


class Search(db.Model):

    key_word= db.StringProperty()
    location= db.StringProperty()
    created_at = db.DateTimeProperty(auto_now_add=True)


class Tweet(db.Model):
    text = db.TextProperty()
    from_user= db.StringProperty()
    from_user_name= db.StringProperty()
    created_at = db.StringProperty()
    loation = db.StringProperty()
    image=db.StringProperty()
    weight=db.FloatProperty()
    sentiment=db.FloatProperty()

class HighHit(db.Model):
    word=db.StringProperty()
    search=db.ReferenceProperty(Search)

class HittoTweet(db.Model):
    tweet=db.ReferenceProperty(Tweet)
    highhit=db.ReferenceProperty(HighHit)
