# 04. The marks obtained by a student in 5 different subjects are input through the keyboard. The student gets a division as per the following rules: Write a program to calculate the division obtained by the student.

# Percentage above or equal to 60 - First division
# Percentage between 50 and 59 - Second division
# Percentage between 40 and 49 - Third division
# Percentage less than 40 – Fail


m1=int(input("Enter the Mark Subject 1 :"))
m2=int(input("Enter the Mark Subject 2 :"))
m3=int(input("Enter the Mark Subject 3 :"))
m4=int(input("Enter the Mark Subject 4 :"))
m5=int(input("Enter the Mark Subject 5 :"))
total=m1+m2+m3+m4+m5
per=total/5
print("Total :",total)
print("Percentage :",per)
if(per>=60):
	print("First Division..")
elif(per>=50 and per<=59):
	print("Second Division..")
elif(per>=40 and per<=49):
	print("Third Division..")
else:
	print("Fail..")