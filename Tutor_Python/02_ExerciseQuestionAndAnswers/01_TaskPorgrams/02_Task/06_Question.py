# 06. Write a program to calculate the salary as per the following table:

# Gender	Year of Service	Qualifications	Salary
# Male	>= 10	Post - Graduate	15000
# >= 10	Graduate	10000
# < 10	Post - Graduate	10000
# < 10	Graduate	7000
# Female	>= 10	Post - Graduate	12000
# >= 10	Graduate	9000
# < 10	Post - Graduate	10000
# < 10	Graduate	6000


gen = input("Enter the Gender f/m :")
yos = int(input("Enter the Years of Service :"))
qual = int(input("Enter the Qualification (Graduate(0) , Post-Graduate(1)) :"))
if(gen=='m' and yos>=10 and qual==1):
	salary = 15000	
	print("Salary : " , salary)
elif( (gen=='m' and yos>=10 and qual==0) or ( gen=='m' and yos<10 and qual==1 ) or ( gen=='f' and yos<10 and qual==1)):
	salary = 10000	
	print("Salary : " , salary)
elif( gen=='m' and yos<10 and qual==0):
	salary = 7000	
	print("Salary : " , salary)
elif( gen=='f' and yos>=10 and qual==1):
	salary = 12000	
	print("Salary : " , salary)
elif( gen=='f' and yos>=10 and qual==0):
	salary = 9000	
	print("Salary : " , salary)
elif( gen=='f' and yos<10 and qual==0):
	salary = 6000	
	print("Salary : " , salary)