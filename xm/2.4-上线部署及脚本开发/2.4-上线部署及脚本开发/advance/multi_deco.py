'''
多层装饰器叠加

    如：
        flask

        @route('/user/info/')
        @login_required
        def user_info():
            pass
'''

def deco1(func):
    print('exec deco1(%s)' % func.__name__)
    def wrap1(*args, **kwargs):
        print('exec wrap1')
        result = func(*args, **kwargs)
        print('exit wrap1')
        return result
    print('exit deco1')
    return wrap1


def deco2(func):
    print('exec deco2(%s)' % func.__name__)
    def wrap2(*args, **kwargs):
        print('exec wrap2')
        result = func(*args, **kwargs)
        print('exit wrap2')
        return result
    print('exit deco2')
    return wrap2


def deco3(func):
    print('exec deco3(%s)' % func.__name__)
    def wrap3(*args, **kwargs):
        print('exec wrap3')
        result = func(*args, **kwargs)
        print('exit wrap3')
        return result
    print('exit deco3')
    return wrap3


@deco1
@deco2
@deco3
def power(x, y):
    return x ** y

print('装饰完成')


power(3, 2)
print('执行完成')

print('-------------------------------------------')

def rewop(x, y):
    return x ** y


# 装饰
wrap3 = deco3(rewop)
wrap2 = deco2(wrap3)
wrap1 = deco1(wrap2)
rewop = wrap1
print('装饰完成')

# 执行
rewop(3, 2)
print('执行完成')
