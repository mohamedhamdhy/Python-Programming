class user:
    course = 'Java'
 
 
o = user()
print(user.__dict__)
print(user.course)  # Print Class attribute
print(o.__dict__)
print(o.course)
o.course = "C++"
print(o.__dict__)
print(o.course)
 
o2 = user()
print(o2.course)