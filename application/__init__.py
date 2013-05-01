#-*- coding:utf-8 -*-
from flask import Flask
from . import config
# from flask_debugtoolbar import DebugToolbarExtension
#from gae_mini_profiler import profiler, templatetags
from werkzeug.debug import DebuggedApplication


app = Flask(__name__, static_folder='../static',
            template_folder='../templates')
app.config.from_object(config.DevelopmentConfig)

from . import views
