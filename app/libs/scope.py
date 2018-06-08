# -*- coding:utf-8 -*-
__author__ = 'gjw'
__date__ = '2018/6/8 10:40'


class Scope:
    # 加入其它的scope
    def add(self, other):
        self.allow_api += other.allow_api
        # 为进行链式add而加入返回值
        return self


class AdminScope(Scope):
    allow_api = ["v1.super_get_user"]

    def __init__(self):
        self.add(UserScope())


class UserScope(Scope):
    allow_api = ['v1.A', 'v1.B']


class SuperScope(Scope):
    allow_api = ['v1.C', 'v1.D']

    def __init__(self):
        # 可以方便的加入新的scope
        self.add(UserScope()).add(AdminScope())


SuperScope()
AdminScope()

def is_in_scope(scope, endpoint):
    # 通过globals()实现反射
    # 将当前所有模块下的变量、类都变成字典
    # gl = globals()
    # 获取scope对象
    scope = globals()[scope]()
    if endpoint in scope.allow_api:
        return True
    pass