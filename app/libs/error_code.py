# -*- coding:utf-8 -*-
from werkzeug.exceptions import HTTPException

from app.libs.error import APIException

__author__ = 'gjw'
__date__ = '2018/5/24 16:42'


class Success(APIException):
    code = 201
    msg = 'ok'
    error_code = 0


class ClientTypeError(APIException):
    code = 400
    msg = 'client is invalid'
    error_code = 1006


class ParameterException(APIException):
    code = 400
    msg = 'invalid parameter'
    error_code = 1000


class NotFound(APIException):
    code = 404
    msg = 'the resource are not_found 0_0...'
    error_code = 1001


class AuthFailed(APIException):
    code = 401
    error_code = 1005
    msg = 'authorization failed'
