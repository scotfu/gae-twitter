#-*- coding:utf-8 -*-
import os
from flask import Flask
from . import config
from flask_debugtoolbar import DebugToolbarExtension
from gae_mini_profiler import profiler, templatetags
from werkzeug.debug import DebuggedApplication


## Extensions
app = Flask(__name__, static_folder='../static',
            template_folder='../templates')


app.config.from_object(config.DevelopmentConfig)

if app.debug:
    app.wsgi_app = DebuggedApplication(app.wsgi_app, True)


from . import views
