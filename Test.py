class Test:
    def __init__(self):
        pass

    def m1(self):
        print('m1')

    def m2(self):
        print('m1')

    def m3(self):
        print('m1')

    def m4(self):
        test = {'a':self.m1,
                'b':self.m2
                }
        test['a']()

obj = Test()
obj.m4()
