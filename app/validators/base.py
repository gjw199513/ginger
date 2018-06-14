# -*- coding:utf-8 -*-
from flask import request
from wtforms import Form

from app.libs.error_code import ParameterException

__author__ = 'gjw'
__date__ = '2018/5/24 17:29'


class BaseForm(Form):
    def __init__(self):
        # data = request.json
        # 静默模式，无法序列化时不会抛异常
        data = request.get_json(silent=True)
        args = request.args.to_dict()
        super(BaseForm, self).__init__(data=data, **args)

    def validate_for_api(self):
        valid = super(BaseForm, self).validate()
        if not valid:
            # 将form中的错误抛出异常
            raise ParameterException(msg=self.errors)
        # 返回form
        return self
