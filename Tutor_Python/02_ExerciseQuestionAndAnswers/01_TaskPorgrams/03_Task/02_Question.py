# 02. Write a program to find whether the given number is prime or not

"""num = int(input("Enter the Number :"))
if num > 1:
 
	for i in range(2, num+1):
		if (num % i) == 0:
			print(num, "is not a prime number")
			break
	else:
		print(num, "is a prime number")
 
else:
	print(num, "is not a prime number")
 
"""
x = int(input("Enter a number: "))
sum=0
for i in range(1, x + 1):
       if x % i == 0:
           sum=sum+1
if(sum==2):
	print("This is a Prime Number")
else:
	print("This is a Not Prime Number")