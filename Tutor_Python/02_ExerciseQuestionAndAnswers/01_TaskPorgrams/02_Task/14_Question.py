# 14. Any year is entered through the keyboard, write a program to determine whether the year is leap or not. Use the logical operators && and ||.

year = int(input("Enter the Year :")) 
if (year%4 == 0 and year%100 != 0) or (year%400 == 0):
	print("Given Year is a leap Year")
else:  
	print ("Given Year is not a leap Year")  