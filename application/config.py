#-*- coding:utf-8 -*-
class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = 'development key'
    DATABASE_URI = 'mysql://fu@localhost/youtube'
    UPLOAD_FOLDER = '/home/ubuntu/myyoutube/static/uploads/'
    ALLOWED_EXTENSIONS = set(['mp4', 'mkv', 'avi','mov'])
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024
    S3_BUCKET_NAME = u'youtube'
    RDS= True
    CLOUDFORNT = True
    S3=True

class DevelopmentConfig(Config):
    DEBUG = True
    PAGE = 15

class TestingConfig(Config):
    TESTING = True
