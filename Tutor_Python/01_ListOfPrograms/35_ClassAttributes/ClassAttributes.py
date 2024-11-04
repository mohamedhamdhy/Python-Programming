class Student():
    name = "Ram Kumar"
    age = 25
 
 
''' This is Class Attributes '''
 
# getattr method
print(getattr(Student, 'name'))
print(getattr(Student, 'age'))
print(getattr(Student, 'gender', 'No Such Attribute Found'))
 
# Dot Notation
print(Student.name)
print(Student.age)
 
# setattr
setattr(Student, 'name', 'Tutor Joes')
print(Student.name)
 
setattr(Student, 'gender', 'Male')
print(Student.gender)
 
Student.city = "Salem"
print(Student.city)
 
print(Student.__dict__)
delattr(Student,"city")
print(Student.__dict__)
del Student.gender
print(Student.__dict__)
 