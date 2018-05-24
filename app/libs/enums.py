# -*- coding:utf-8 -*-
from enum import Enum

__author__ = 'gjw'
__date__ = '2018/5/24 15:04'


class ClientTypeEnum(Enum):
    USER_EMAIL = 100
    USER_MOBILE = 101

    # 微信小程序
    USER_MINA = 200
    # 微信公众号
    USER_WX = 201
