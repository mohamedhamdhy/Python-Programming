# 06. Write a program to find the reverse of n digit number using While loop

num = int(input("Enter the Number :"))
a=num
sum=0
while(num>0):
	rem=num%10
	sum=(sum*10)+rem
	num=num//10
print("Before Number :",a)
print("Reverse Number :",sum)