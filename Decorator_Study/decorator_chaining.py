def decor1(func):

    def inner(name):
        print("Decorator1 Executing")
        func(name)
    return inner


def decor2(func):

    def inner(name):
        print("decorator2 is executing")
        func(name)
    return inner


@decor2
@decor1
def wish(name):
    print("Hello", name , "good morning")


wish("HS")

