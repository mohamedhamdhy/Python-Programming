# 03. Write a program to find the given number is Armstrong number or not

num = int(input("Enter the Number :"))
a=num
sum=0
while(num>0):
	rem=num%10
	sum=sum+(rem*rem*rem)
	num=num//10
if(sum==a):
	print(a, "is a Armstrong Number")
else:
	print(a, "is a Not Armstrong Number")
