# 5. The length & breadth of a rectangle and radius of a circle are input through the keyboard. Write a program to calculate the area & perimeter of the rectangle, and the area & circumference of the circle.

'''
Area of Rectangle=l*b
Perimeter of Rectangle=2*(l+b)
Area of Circule=PI*r*r(PI=3.14)
Circum of a Circule=2*PI*r
'''
len=int(input("Enter the Lenth of rectangle:"))
bre=int(input("Enter the Breadth of rectangle:"))
r=int(input("Enter the Redius of Circle:"))
area1=len*bre
perimeter=2*(len+bre)
area2=3.14*r*r
circum=2*3.14*r
print("Area of Rectangle =",area1)
print("Perimeter of Rectangle =",perimeter)
print("Area of Circle =",area2)
print("Circum of Circle =",circum)