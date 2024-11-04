class A:
    def display(self):
        print("I am the display of Class A")
 
 
class B(A):
    def display(self):
        print("I am the display of Class B")
 
 
class C(A):
    def display(self):
        print("I am the display of Class C")
 
 
class D(B, C):
    def display(self):
        print("I am the display of Class D")
 
 
o = D()
o.display()