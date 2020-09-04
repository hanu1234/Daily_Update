class Test:
        def __init__(self):
                pass
        def m1(self, a=None, **kwargs):
                print(a)
                print(kwargs)


obj = Test()
obj.m1(m=30, c=20)