# -*- coding:utf-8 -*-
from flask import g
from flask.json import jsonify

from app.libs.error_code import DeleteSuccess, AuthFailed
from app.libs.redprint import Redprint
from app.libs.token_auth import auth
from app.models.base import db
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
def super_get_user(uid):
    # is_admin = g.user.is_admin
    # if not is_admin:
    #     raise AuthFailed()
    # token是否合法 是否过期
    user = User.query.filter_by(id=uid).first_or_404()
    # jsonify对于不知道如何序列化的对象，会调用default函数
    return jsonify(user)


@api.route("", methods=["GET"])
@auth.login_required
def get_user():
    uid = g.user.id
    user = User.query.filter_by(id=uid).first_or_404()
    return jsonify(user)


# 管理员
@api.route("/<int:uid>", methods=["DELETE"])
def super_delete_user(uid):
    pass


@api.route("", methods=["DELETE"])
@auth.login_required
def delete_user():
    # 防止超权，用户只能删除自己
    # g变量是线程隔离的，不会发生数据错乱
    uid = g.user.uid
    with db.auto_commit():
        # 使用自定义的filter_by,可以加入状态码值的判断条件
        user = User.query.filter_by(id=uid).first_or_404()
        user.delete()
    return DeleteSuccess()


