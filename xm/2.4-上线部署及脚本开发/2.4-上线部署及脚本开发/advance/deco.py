'''
定义一个装饰器，确保被装饰函数的返回值是一个非负数，如果返回值是负数，直接返回 0
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


@check  # 语法糖
def foo():
    '''this is foo'''
    n = random.randint(-10, 10)
    print('n = %s' % n)
    return n


def bar():
    '''this is bar'''
    m = random.randint(-10, 10)
    print('m = %s' % m)
    return m


# 装饰
wrap = check(bar)
bar = wrap
# 执行
bar()
