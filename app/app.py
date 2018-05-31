# -*- coding:utf-8 -*-
from flask import Flask as _Flask
from flask.json import JSONEncoder as _JSONEncoder
from app.libs.error_code import ServerError
from datetime import date
__author__ = 'gjw'
__date__ = '2018/5/24 11:16'


# 重写原来的JSONEncoder
class JSONEncoder(_JSONEncoder):
    def default(self, o):
        if hasattr(o, 'keys') and hasattr(o, '__getitem__'):
            return dict(o)
        # 对不能序列化的日期类型进行判断并处理
        if isinstance(o, date):
            return o.strftime('%Y-%m-%d')
        raise ServerError()


# 把flask中原来的JSONEncoder，替换为自己定义的JSONEncoder
class Flask(_Flask):
    json_encoder = JSONEncoder


