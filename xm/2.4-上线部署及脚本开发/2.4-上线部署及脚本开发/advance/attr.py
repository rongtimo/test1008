class User:
    '''TestClass'''
    z = [7, 8, 9]

    def __init__(self):
        self.x = 100
        self.y = 'abc'
        self.money = 1000.0

    def __setattr__(self, name, value):
        if name == 'money':
            if not isinstance(value, float):
                raise TypeError('money must be float')
            if value < 0:
                raise ValueError('money < 0')

        print('setattr: %s = %s' % (name, value))
        object.__setattr__(self, name, value)

    def __getattribute__(self, name):
        print('getattribute: %s' % name)
        return object.__getattribute__(self, name)

    def __getattr__(self, name):
        print('getattr: %s' % name)
        return -1

    def foo(self, x, y):
        return x ** y
