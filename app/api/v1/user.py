# -*- coding:utf-8 -*-
from flask.json import jsonify

from app.libs.redprint import Redprint
from app.libs.token_auth import auth
from app.models.user import User

__author__ = 'gjw'
__date__ = '2018/5/24 11:54'


api = Redprint('user')


# class Gjw:
#     name = 'gjw'
#     age = 18
#
#     def __init__(self):
#         self.gender = 'male'
#
#     # 获得字典的键
#     def keys(self):
#         # 可以控制返回的属性
#         return ['name', 'age', 'gender']
#
#     # 获得字典的值
#     def __getitem__(self, item):
#         return getattr(self, item)


@api.route('/<int:uid>', methods=["GET"])
@auth.login_required
def get_user(uid):
    # token是否合法 是否过期
    user = User.query.get_or_404(uid)
    # jsonify对于不知道如何序列化的对象，会调用default函数
    return jsonify(user)


@api.route('/create')
def create_user():
    pass
# 用户 注册
