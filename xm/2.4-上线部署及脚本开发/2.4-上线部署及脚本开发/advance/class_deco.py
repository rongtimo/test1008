'''
通过类构造装饰器
'''

import random


def check(func):
    '''this is check'''
    def wrap(*args, **kwargs):
        '''this is wrap'''
        n = func(*args, **kwargs)
        if n < 0:
            return 0
        else:
            return n
    return wrap


class Check:
    '''类构造的装饰器'''
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        '''this is __call__'''
        n = self.func(*args, **kwargs)
        if n < 0:
            return 0
        else:
            return n


@Check
def foo():
    '''this is foo'''
    n = random.randint(-10, 10)
    print('n = %s' % n)
    return n


# 函数装饰过程
wrap = check(foo)
wrap()

# 通过类去装饰过程
obj = Check(foo)
obj()
