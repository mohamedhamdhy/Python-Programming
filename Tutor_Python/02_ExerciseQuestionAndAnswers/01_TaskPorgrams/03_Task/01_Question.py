# 01. Write a program to find the factor of the given number

x = int(input("Enter the Number :"))
for i in range(1, x + 1):
       if x % i == 0:
           print(i)