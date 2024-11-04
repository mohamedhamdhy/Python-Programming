# 04. Write a program to print the Armstrong numbers between 100 to 999

for i in range(100,999):
	a=i
	sum=0
	while(i>0):
		rem=i%10
		sum=sum+(rem*rem*rem)
		i=i//10
	if(sum==a):
		print(a, "is a Armstrong Number")