# 1. While purchasing certain items, a discount of 10% is offered if the quantity purchased is more than 10. If quantity and price per item are input through the keyboard, write a program to calculate the total expenses.

qty = int(input("Enter the Quantity Purchased :"))
amt = float(input("Enter the Amount Per Item :"))
if(qty>10):
	total = qty * amt; 
	total = total- (total * 0.1)
else:
	total = qty * amt
 
print("Total Expenses is :",total)