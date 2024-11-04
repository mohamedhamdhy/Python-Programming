# 11. Write a program to check whether a triangle is valid or not, when the three angles of the triangle are entered through the keyboard. A triangle is valid if the sum of all the three angles is equal to 180 degrees.

s1 = int(input("Enter the Triangle Side-1 :"))
s2 = int(input("Enter the Triangle Side-2 :"))
s3 = int(input("Enter the Triangle Side-3 :"))
sum = s1+s2+s3
if(sum==180):
	print("Triangle Valid..")
else:
	print("Triangle Not Valid..")