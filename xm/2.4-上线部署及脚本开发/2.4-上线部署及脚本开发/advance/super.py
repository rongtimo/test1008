class A:
    def __init__(self):
        print('enter A')
        self.x = 111
        print('exit A')


class B(A):
    def __init__(self):
        print('enter B')
        self.y = 222
        super().__init__()
        print('exit B')


class C(A):
    def __init__(self):
        print('enter C')
        self.z = 333
        super().__init__()
        print('exit C')


class D(B, C):
    def __init__(self):
        print('enter D')
        super().__init__()
        print('exit D')

d = D()

'''
期待的顺序
    enter D
    enter B
    enter C
    enter A
    exit A
    exit C
    exit B
    exit D
'''
print(D.mro())
