# -*- coding:utf-8 -*-
from flask import Blueprint

from app.libs.redprint import Redprint

__author__ = 'gjw'
__date__ = '2018/5/24 11:54'


# redprint
api = Redprint('book')


@api.route('', methods=['GET'])
def get_book():
    return 'get book'


@api.route('', methods=['POST'])
def create_book():
    return 'create book'