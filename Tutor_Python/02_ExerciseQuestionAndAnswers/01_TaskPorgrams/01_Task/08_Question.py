# 08. If a five-digit number is input through the keyboard, write a program to reverse the number.

n=int(input("Enter the five digits Number:"))
revnum=0
a=n%10
n=n//10
revnum=revnum+a*10000
 
a=n%10
n=n//10
revnum=revnum+a*1000
 
a=n%10
n=n//10
revnum=revnum+a*100
 
a=n%10
n=n//10
revnum=revnum+a*10
 
a=n%10
revnum=revnum+a
 
print("Reverse Five digits =",revnum)