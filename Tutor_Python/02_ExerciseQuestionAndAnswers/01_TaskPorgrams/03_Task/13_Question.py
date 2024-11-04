# 13. Write a program to find the given number is strong number


num = int(input("Enter the Number :"))
a=num
sum=0
while (num>0):
	rem=num%10;
	fact=1;
	for i in range(1,rem+1):
		fact=fact*i
	sum=sum+fact;
	num=num//10;
if (sum == a):
	print(a,"is Strong Number");
else:
	print(a ,"is not a Strong Number");