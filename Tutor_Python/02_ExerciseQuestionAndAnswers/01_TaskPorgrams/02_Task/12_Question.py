# 12. Find the absolute value of a number entered through the keyboard

num = int(input("Enter the Number :"))
#print("Absolute Number :",abs(num))
if(num<0):
	num = (-1)*num
print("Absolute Number :",num)