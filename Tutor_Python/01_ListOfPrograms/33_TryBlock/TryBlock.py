"""
# try block in Python
try:
    a = 10 / 0
except Exception as e:
    print(e)
 
# Try Else
try:
    a = 10 / 25
except Exception as e:
    print(e)
else:
    print("A Value : ",a)
 
# Try else finally
try:
    a = 10 / 0
except Exception as e:
    print(e)
else:
    print("A Value : ",a)
finally:
    print("Thank You")
 
 
# Type of Exceptions in Python
print(dir(locals()['__builtins__']))
print(len(dir(locals()['__builtins__'])))
 
# Nameerror Exception
 
 
try:
    print(a)
except NameError as e:
    print("A is not Defined")
 
try:
    print(10 / 0)
except ZeroDivisionError as e:
    print("denominator cant be zero")
 
try:
    a = int("Joes")
except ValueError as e:
    print("Please Enter Numbers only")
 
try:
    a = [10, 20, 30, 40]
    print(a[10])
except IndexError as e:
    print("Invalid Index")
 
try:
    f = open("tesot.txt")
except FileNotFoundError:
    print("File Not Found")
else:
    print(f.read())
"""
 
try:
    a=10/20
    print(a)
    b=[10,20,30,40]
    print(b[0])
    a=open('ramu.txt')
except ZeroDivisionError:
    print("denominator cant be zero")
except IndexError:
    print("Invalid Index")
except Exception as e:
    print(e)
 