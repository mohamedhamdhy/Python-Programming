# 13. Given the length and breadth of a rectangle, write a program to find whether the area of the rectangle is greater than its perimeter. For example, the area of the rectangle with length = 5 and breadth = 4 is greater than its perimeter


len = float(input("Enter the Length : "))
bre = float(input("Enter the Breadth : "))
area = len * bre;
perimeter = 2 * (len+bre)
print("Area of Rectangle :", area)
print("Perimeter of Rectangle :", perimeter)
if (area>perimeter):
	print("Area of rectangle is greater than  Perimeter")
else:
	print("Perimeter of rectangle is greater than Area")