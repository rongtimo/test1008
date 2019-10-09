'''
Python 编码规范
'''

import sys
import os

from django.conf import settings

from user.models import *

MOD = 0xffffffff


def foo(age, box=123):
    '''this is foo'''
    c = {'x': 111, 'y': 222}  # 定义一个字典
    d = [1, 3, 5]
    box = {i * 3: j * 5
           for i, j in zip(range(10), range(20, 40))
           if i % 2 == 0 and j % 2 == 1}
    return a, b, c


def bar(x):
    '''this is bar'''
    if x % 2 == 0:
        return True
