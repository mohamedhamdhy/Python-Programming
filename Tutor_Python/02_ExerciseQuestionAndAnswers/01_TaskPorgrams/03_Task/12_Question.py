# 12. Write a program to print the perfect number between 1-1000

num = 1000
for i in range(1, num):
       if num % i == 0:
           print(i)