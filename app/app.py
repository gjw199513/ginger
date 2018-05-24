# -*- coding:utf-8 -*-
from flask import Flask

__author__ = 'gjw'
__date__ = '2018/5/24 11:16'


def register_blueprint(app):
    from app.api.v1 import create_blueprint_v1
    app.register_blueprint(create_blueprint_v1(), url_prefix='/v1')


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.setting')
    app.config.from_object('app.config.secure')

    register_blueprint(app)
    return app