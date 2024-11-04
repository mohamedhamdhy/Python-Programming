"""
is
is not
"""
a = [1, 2]
b = [1, 2]
c = a
print(id(a))
print(id(c))
print(id(b))
print(a is c)
print(a is b)
print(a==b)
print(a is not c)
print(a is not b)
print(a!=b)