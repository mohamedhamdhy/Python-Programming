# Tuple in Python
# Immutable
# Surrounded by Round Brackets (1,1,5)

a = (1, 2.5, True, "Ram")
print(a)
print(type(a))
print(a[1])
print(a[-1])
print(a[0:2])
b = list(a)
print(b)
b.append("Raja")
print(b)
print(type(b))
a = tuple(b)
print(a)
print(type(a))

for i in a:
    print(i)

if "Raj" in a:
    print("Raja is Found")
else:
    print("Not Found")
print(len(a))

a = (1,)
print(type(a))
del a
a = (1, 2, 7, 4)
b = (5, 6, 7, 8)
c = a + b
print(c)
print(c.count(7))

a = (1, 2, 7, 4)
b = (5, 6, 7, 8)
c = (a, b)
print(c)
print(c[0])
print(c[1])
print(c[0][1])
x = ('Joes',) * 10
print(x)

a = (1, 2, 7, 4)
b = (5, 6, 7, 8)
print(min(a))
print(max(a))