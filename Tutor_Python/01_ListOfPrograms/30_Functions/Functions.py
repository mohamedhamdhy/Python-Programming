def welcome():
    print("Welcome To Tutor Joes")
 
 
welcome()
 
# No Return Type Without Argument Function in Python
"""
def add():
    a=int(input("Enter The Value of A : "))
    b=int(input("Enter The Value of B : "))
    c=a+b
    print("Total ",c)
 
add()
"""
 
# No Return Type With Argument Function in Python
"""
def sub(a, b):
    c = a - b
    print("Difference : ", c)
 
 
sub(25, 2)
"""
 
# Return Type Without Argument Function in Python
"""
def mul():
    a = int(input("Enter The Value of A : "))
    b = int(input("Enter The Value of B : "))
    c = a * b
    return c
 
 
x=mul()
print("Mul ",x)
"""
 
# Return Type With Argument Function in Python
"""
def div(a, b):
    c = a / b
    return c
 
 
x = div(25, 2)
print("Division ", x)
"""
 
# Arbitrary Arguments Function in Python (*)
"""
def class_10(*students):
    print(students)
    for user in students:
        print(user)
 
 
class_10("Ram", "Sam", "Raja", "Sara")
"""
 
# Keyword Arguments Function in Python
 
"""
def message(name, age):
    print(name, " age is ", age)
 
 
message(age=25, name="Ram")
"""
 
# Arbitrary Keyword Arguments in Python(**)
"""
def bioData(**data):
    print(data)
 
 
bioData(name="Ram Kumar", age=25, gender="Male")
"""
 
# Default Parameter Function in Python
"""
def user(name, city="Salem"):
    print(name, " is from ", city)
 
 
user("Ram", "Namakkal")
user("Sam")
"""
 
# Passing a List as an Argument in Function Python
"""
def total(marks):
    return sum(marks)
 
 
print("Total : ",total([55, 75, 80, 95, 47]))
"""
 
# recursive function
# 1 * 2 * 3 * 4 * 5=120
"""
def factorial(x):
    if x == 1:
        return 1
    else:
        return (x * factorial(x - 1))
 
 
print("Factorial : ", factorial(5))
"""
"""
factorial(5)
5*factorial(4)
5*4*factorial(3)
5*4*3*factorial(2)
5*4*3*2*factorial(1)
5*4*3*2*1
120
"""
 
c = lambda a: a + 50
print(c(5))
 
c = lambda a, b: a * b
print(c(10, 25))