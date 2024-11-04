# 9. If a four-digit number is input through the keyboard, write a program to obtain the sum of the first and last digit of this number.

n=int(input("Enter the four Digits Number :"))
sum=0
a=n//1000
sum=sum+a
a=n%10
sum=sum+a
print("Sum of First and Last digits =",sum)
