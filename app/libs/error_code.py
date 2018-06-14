# -*- coding:utf-8 -*-
from werkzeug.exceptions import HTTPException

from app.libs.error import APIException

__author__ = 'gjw'
__date__ = '2018/5/24 16:42'


class Success(APIException):
    code = 201
    msg = 'ok'
    error_code = 0


class DeleteSuccess(Success):
    # 204为restful的删除返回码，实际不返回任何值
    # code = 204

    # 为了保证标准的返回，返回202
    code = 202
    error_code = 1


class ServerError(APIException):
    code = 500
    msg = 'sorry, we make a mistake (*- - )!'
    error_code = 999


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


class Forbidden(APIException):
    code = 403
    error_code = 1004
    msg = 'forbidden, not in scope'


class DuplicateGift(APIException):
    code = 400
    error_code = 2001
    msg = 'the current book has already in gift'
