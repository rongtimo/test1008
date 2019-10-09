class Test(object):
    x = 123

    def __init__(self):
        self.y = 456

    def bar1(self):
        print('i am a method')

    @classmethod
    def bar2(cls):
        print('i am a classmethod')

    @staticmethod
    def bar3():
        print('i am a staticmethod')

    def foo1(self):
        print(self.x)
        print(self.y)
        self.bar1()
        self.bar2()
        self.bar3()

    @classmethod
    def foo2(cls):
        print(cls.x)
        # print(cls.y)
        # cls.bar1()
        cls.bar2()
        cls.bar3()

    @staticmethod
    def foo3(obj):
        print(obj.x)
        print(obj.y)
        obj.bar1()
        obj.bar2()
        obj.bar3()

t = Test()
# t.foo1()
# t.foo2()
t.foo3(t)
