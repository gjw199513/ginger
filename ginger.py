# -*- coding:utf-8 -*-
from werkzeug.exceptions import HTTPException

from app import create_app
from app.libs.error import APIException

__author__ = 'gjw'
__date__ = '2018/5/24 11:16'


app = create_app()


# 全局异常信息处理
@app.errorhandler(Exception)
def framework_error(e):
    if isinstance(e, APIException):
        return e
    if isinstance(e, HTTPException):
        code = e.code
        msg = e.description
        error_code = 1007
        return APIException(msg, code, error_code)
    else:
        # 真实环境需要日志记录
        if not app.config['DEBUG']:
            return APIException()
        else:
            raise e


@app.route('/v1/user/get')
def get_user():
    return 'i am'


if __name__ == '__main__':
    app.run(debug=True)