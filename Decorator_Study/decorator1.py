"""
--> Decorator is a design pattern in python which allows user to add new functionality to the existing object without
modifying its structure.

--> Functions in python are first class citizens. means hat they support operations such as being passed as an argument,
 returned from a function, modified, and assigned to a variable.

Input function ==> Decorator Function ==> output function with extended functionality

"""


def outer():
    print("Outer function started")

    def inner():
        print("Inner function execution")

    print("outer function returning inner function")
    return inner


f1 = outer()  # outer function returned the inner function to f1 variable

f1()  # f1 is inner function. so calling the inner function
