# -*- coding:utf-8 -*-
from flask import Blueprint

from app.libs.redprint import Redprint
from app.libs.token_auth import auth
from app.models.user import User

__author__ = 'gjw'
__date__ = '2018/5/24 11:54'


api = Redprint('user')


@api.route('/<int:uid>', methods=["GET"])
@auth.login_required
def get_user(uid):
    # token是否合法 是否过期
    user = User.query.get_or_404(uid)
    return 'i am user'


@api.route('/create')
def create_user():
    pass
# 用户 注册
