"""
==   operator  checks for value equality
is   operator  checks for  whether both the operands refers to the same object or not
"""

l1 = []
l2 = []
l3 = l2

if l1 == l2 :
    print("True")
else:
    print("False")

if l1 is l2:
    print("True")
else:
    print("False")

if l2 is l3:
    print("True")
else:
    print("False")

print(id(l1))
print(id(l2))
print(id(l3))