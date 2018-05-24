# -*- coding:utf-8 -*-
from flask import Blueprint

from app.libs.redprint import Redprint

__author__ = 'gjw'
__date__ = '2018/5/24 11:54'


api = Redprint('user')

@api.route('/get')
def get_user():
    return 'i am user'