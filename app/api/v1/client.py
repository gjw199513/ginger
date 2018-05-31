# -*- coding:utf-8 -*-
from flask import request

from app.validators.forms import ClientForm, UserEmailForm
from app.libs.enums import ClientTypeEnum
from app.libs.error_code import ClientTypeError, Success
from app.libs.redprint import Redprint
from app.models.user import User

__author__ = 'gjw'
__date__ = '2018/5/24 15:01'

api = Redprint('client')


@api.route('/register', methods=["POST"])
def create_client():
    # data = request.json
    # 使用json，需要传入data关键字参数

    form = ClientForm().validate_for_api()
    promise = {
        ClientTypeEnum.USER_EMAIL: __register_user_by_email
    }
    promise[form.type.data]()
    return Success()


def __register_user_by_email():
    form = UserEmailForm().validate_for_api()
    User.register_by_email(form.nickname.data, form.account.data, form.secret.data)
