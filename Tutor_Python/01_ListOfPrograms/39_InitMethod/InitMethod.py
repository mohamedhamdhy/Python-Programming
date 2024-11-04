# init method in Python
 
class user:
    def __init__(self, name):
        print("Call When new Instance Created")
        self.name = name
 
    def printall(self):
        print("Name : ", self.name)
 
 
o1 = user("Tutor Joes")
 
o1.printall()
print(o1.__dict__)
o2 = user("Joes")
o2.printall()
print(o2.__dict__)
print(user.__dict__)
 