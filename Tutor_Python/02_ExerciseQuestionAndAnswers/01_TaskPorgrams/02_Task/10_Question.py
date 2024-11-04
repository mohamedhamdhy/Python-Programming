# 10. If the ages of Ram, Shyam and Ajay are input through the keyboard, write a program to determine the youngest of the three.

age1 = int(input("Enter the Age of Ram :"))
age2 = int(input("Enter the Age of Shyam :"))
age3 = int(input("Enter the Age of Ajay :"))
if(age1<age2 and age1<age3):
	print("The Youngest Age is Ram")
elif(age2<age1 and age2<age3):
	print("The Youngest Age is Shyam")
else:
	print("The Youngest Age is Ajay")