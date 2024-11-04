# Static Method in Python
 
class student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
 
    def printDetail(self):
        print("Name : ", self.name, "  Age : ", self.age)
 
    @staticmethod
    def welcome():
        print("Welcome to our Institution")
 
 
s1 = student("Joes", 25)
s1.printDetail()
s1.welcome()
 
 
s2 = student("Raja", 45)
s2.printDetail()
s2.welcome()