# 08. Any integer is input through the keyboard. Write a program to find out whether it is an odd number or even number. (Hint: Use the % (modulus) operator)

num = int(input("Enter the Number: "))
if num % 2 == 0:
    print(num, "is an Even Number")
else:
    print(num, "is an Odd Number")
