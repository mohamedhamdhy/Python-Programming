# 2. The distance between two cities (in km.) is input through the keyboard. Write a program to convert and print this distance in meters, feet, inches and centimeters.

'''
Formulas:
meters = kilometers × 1000
centimeters = meters × 100
inches = centimeters ÷ 2.54
feet = inches ÷ 12
'''
km=float(input("Enter The Kilometer : "));
m=km*1000;
cm=m*100;
i=cm/2.54;
ft=i/12;
print("Kilometers : ",km);
print("Meters  : ",m);
print("Centimeters : ",cm);
print("Inches : ",i);
print("Feet : ",ft);