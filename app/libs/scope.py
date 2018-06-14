# -*- coding:utf-8 -*-
__author__ = 'gjw'
__date__ = '2018/6/8 10:40'


class Scope:
    allow_api = []
    allow_module = []
    forbidden = []

    # 加入其它的scope
    # 加号运算符重载
    def __add__(self, other):
        self.allow_api += other.allow_api
        # 去重
        self.allow_api = list(set(self.allow_api))

        # 红图的相加和去重
        self.allow_module = self.allow_module + other.allow_module
        self.allow_module = list(set(self.allow_module))

        # 排除的相加和去重
        self.forbidden = self.forbidden + other.forbidden
        self.forbidden = list(set(self.forbidden))
        # 为进行链式add而加入返回值
        return self


class AdminScope(Scope):
    allow_api = ["v1.user+super_get_user",
                 'v1.user+super_delete_user']
    # allow_module = ['v1.user']

    def __init__(self):
        # # 包含userscope允许访问的api
        # self + UserScope()
        # print(self.allow_api)
        pass


class UserScope(Scope):
    forbidden = ['v1.user+super_get_user',
                 'v1.user+super_delete_user']

    def __init__(self):
        self + AdminScope()
    # allow_api = ['v1.user+get_user', 'v1.user+delete_user']


#


# SuperScope()
# AdminScope()


def is_in_scope(scope, endpoint):
    # 通过globals()实现反射
    # 将当前所class SuperScope(Scope):
    # #     allow_api = ['v1.C', 'v1.D']
    # #     allow_module = ['v1.user']
    # #
    # #     def __init__(self):
    # #         # 可以方便的加入新的scope
    # #         self + UserScope() + AdminScope()
    # #         print(self.allow_api)有模块下的变量、类都变成字典
    # gl = globals()
    # 获取scope对象

    # v1.view_func => v1.module_name+view_func
    # v1.red_name+view_func

    scope = globals()[scope]()
    # 使用加号将red_name和view_func分隔
    splits = endpoint.split('+')
    red_name = splits[0]
    # 排除
    if endpoint in scope.forbidden:
        return False
    # 视图函数
    if endpoint in scope.allow_api:
        return True
    # 红图
    if red_name in scope.allow_module:
        return True
    else:
        return False
