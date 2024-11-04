# instance Methods
class Student:
    name = "Tutor Joes"
    age = 25
 
    def printall(self,gender):
        print("Name : ", Student.name)
        print("Age  : ", Student.age)
        print("Gender  : ", gender)
 
o=Student()
"""
o.printall()
Student.printall(o)
"""
o.printall("Male")
Student.printall(o,"Male")