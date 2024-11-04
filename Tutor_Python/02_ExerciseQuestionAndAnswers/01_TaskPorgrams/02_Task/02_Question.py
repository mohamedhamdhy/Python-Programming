# 02. The current year and the year in which the employee joined the organization are entered through the keyboard. If the number of years for which the employee has served the organization is greater than 3 then a bonus of Rs. 2500/- is given to the employee. If the years of service are not greater than 3, then the program should do nothing.

current_year=int(input("Enter the Current Year :"))
join_year=int(input("Enter the Year of Joining :"))
diff=current_year-join_year
if(diff>3):
	print("Bonus of Rs : 2500 /-");
else:
	print("No Bonus..")