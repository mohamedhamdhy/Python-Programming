# 06.Two numbers are input through the keyboard into two locations C and D. Write a program to interchange the contents of C and D.

c=int(input("Enter the C Values:"))
d=int(input("Enter the D Values:"))
print("Before C Values : ",c)
print("Before D Values : ",d)
a=c
c=d
d=a
print("After C Values:",c)
print("After D Values:",d)
