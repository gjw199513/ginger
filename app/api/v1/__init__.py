# -*- coding:utf-8 -*-
from flask import Blueprint
from app.api.v1 import user, book

__author__ = 'gjw'
__date__ = '2018/5/24 11:54'


def create_blueprint_v1():
    # from app.api.v1.book import api
    # from app.api.v1.user import api
    bp_v1 = Blueprint('v1', __name__)

    user.api.register(bp_v1)
    book.api.register(bp_v1)
    return bp_v1
