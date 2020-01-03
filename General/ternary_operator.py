"""
condition ? value_if_true : value_if_false   basic ternary operator syntax
IN python

[on_true] if [expression] else [on_false]
"""


# Python program to demonstrate nested ternary operator
a, b = 10, 20

print ("Both a and b are equal" if a == b else "a is greater than b" if a > b else "b is greater than a")


# Program to demonstrate conditional operator
a, b = 10, 20

# Copy value of a in min if a < b else copy b
min = a if a < b else b
print(min)

f'hellow world'