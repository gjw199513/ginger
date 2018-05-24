# -*- coding:utf-8 -*-
from werkzeug.exceptions import HTTPException

from app.libs.error import APIException

__author__ = 'gjw'
__date__ = '2018/5/24 16:42'


class ClientTypeError(APIException):
    code = 400
    msg = 'client is invalid'
    error_code = 1006