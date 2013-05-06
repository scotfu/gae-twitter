# /usr/env python
#-*- coding:utf8 -*-

from google.appengine.ext import db

class Tweet(db.Model):
    text = db.StringProperty()
    from_user= db.StringProperty()
    from_user_name= db.StringProperty()
    created_at = db.StringProperty()
    loation = db.StringProperty()
    key_word= db.StringProperty()
    image=db.StringProperty()
    weight=db.FloatProperty()

