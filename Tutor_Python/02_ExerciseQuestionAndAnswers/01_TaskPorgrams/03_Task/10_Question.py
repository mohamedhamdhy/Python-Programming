# 10. Write a program to find the Fibonacci Series of the given number

n = int(input("Enter the Number :"))
n1, n2 = 0, 1
sum = 0
if n <= 0:
   print("Please enter a positive integer")
elif n == 1:
   print("Fibonacci sequence upto",n,":",n1)
else:
   print("Fibonacci sequence:")
   while sum < n:
       print(n1)
       nth = n1 + n2
       n1 = n2
       n2 = nth
       sum += 1