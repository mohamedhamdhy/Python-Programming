# 13. If a five-digit number is input through the keyboard, write a program to print a new number by adding one to each of its digits. For example, if the number that is input is 12391 then the output should be displayed as 23402.


num = int(input("Enter the Five Digits :"))
onum=num
sum = 0
a = (num // 10000)+1
num = num % 10000
sum=sum+(a*10000);
 
a = (num // 1000)+1
num = num % 1000
sum = sum+(a*1000)
 
a = (num // 100)+1
num = num % 100
sum = sum+(a*100)
 
 
a = (num // 10)+1
num = num % 10
sum = sum+(a*10)
 
 
a = num+1
sum = sum+a
print("Old Number :",onum)
print("New Number :",sum)
 
"""
num = int(input("Enter the Five Digits :"))
sum = 0
a = (num // 10000)+1
num = num % 10000
sum=sum+a;
 
a = (num // 1000)+1
num = num % 1000
sum = (sum*10)+a
 
a = (num // 100)+1
num = num % 100
sum = (sum*10)+a
 
 
a = (num // 10)+1
num = num % 10
sum = (sum*10)+a
 
 
a = num+1
sum = (sum*10)+a
print(sum)
"""
