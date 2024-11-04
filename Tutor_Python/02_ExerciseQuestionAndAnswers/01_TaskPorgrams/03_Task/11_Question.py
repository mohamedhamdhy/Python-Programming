# 11. Write a program to find the given number is perfect number

num = int(input("Enter the Number :"))
for i in range(1, num):
       if num % i == 0:
           print(i)