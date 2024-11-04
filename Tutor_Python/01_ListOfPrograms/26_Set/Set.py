names={'Ram','Sam','Ravi'}
print(names)
print(type(names))
# Access Values Using For loop
for name in names:
    print(name)
# Adding New Element
names.add('Sara')
print(names)
# Update Another Set of Data
a={'Kumar','Sundar','Suresh'}
names.update(a)
print(names)
names.remove('Sara')
print(names)
names.discard('Suresh')
print(names)
names.pop()
print(names)
names.clear()
print(names)
del names
names={'Ram','Ram','Sam','Ravi','Kumar','Sundar','Suresh'}
print(names)
a = {1, 2, 3, 4}
b = {'a', 'b', 'c', 'd'}
c=a.union(b)
print(c)
a.update(b)
print(a)
a = {1, 2, 3, 4, 5}
b = {5, 6, 7, 8, 9}
c=a.intersection(b)
print(c)
a.intersection_update(b)
print(a)
c=a.symmetric_difference(b)
print(c)
a.symmetric_difference_update(b)
print(a)
a = {5,6,7}
b = {5, 6, 7}
c=a.isdisjoint(b)
print(c)
c=a.issubset(b)
print(c)
c=a.issuperset(b)
print(c)