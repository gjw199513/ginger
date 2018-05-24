# -*- coding:utf-8 -*-
from flask import request
from wtforms import Form

from app.libs.error_code import ParameterException

__author__ = 'gjw'
__date__ = '2018/5/24 17:29'


class BaseForm(Form):
    def __init__(self):
        data = request.json
        super(BaseForm, self).__init__(data=data)

    def validate_for_api(self):
        valid = super(BaseForm, self).validate()
        if not valid:
            # 将form中的错误抛出异常
            raise ParameterException(msg=self.errors)
        # 返回form
        return self
