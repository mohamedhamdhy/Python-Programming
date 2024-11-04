# 09. A five-digit number is entered through the keyboard. Write a program to obtain the reversed number and to determine whether the original and reversed numbers are equal or not.


num = int(input("Enter the Number :"))
a=num
sum=0
while(num>0):
	rem=num%10
	sum=(sum*10)+rem
	num=num//10
if(a==sum):
	print("Eqaul..")
else:
	print("Not Eqaul..")