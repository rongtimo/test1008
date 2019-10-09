'''
定义一个装饰器，可以检查被装饰函数执行 N 次的时间，N 可以随意指定
'''

import time


def timer(n):
    def warp1(func):
        def wrap2(*args, **kwargs):
            t0 = time.time()
            for i in range(n):
                result = func(*args, **kwargs)
            t1 = time.time()
            print('use %f s' % (t1 - t0))
            return result
        return wrap2
    return warp1


@timer(10000)
def power(x, y):
    return x ** y


def rewop(x, y):
    return x ** y

# 装饰过程
deco = timer(10000)
rewop = deco(rewop)
