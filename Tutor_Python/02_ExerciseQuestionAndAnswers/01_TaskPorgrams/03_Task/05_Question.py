# 05. Write a program to count and print the number of odd and even numbers

l = int(input("Enter the Limit :"))
even=[]
odd=[]
for i in range(l):
	n = int(input("Enter the Values :"))
	if(n%2==0):
		even.append(n)
	else:
		odd.append(n)
print("Number of Even :",len(even))
print("Number of Odd :",len(odd))