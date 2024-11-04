# 07. Write a program to find the binary number from given decimal number


"""
num = input("Enter the Binary Number :")
dec_number= int(num, 2)
print('The binary Number :', num)
print('The decimal Number :', dec_number)
"""
binary = input("Enter the Binary Number :")
decimal = 0
for digit in binary:
    decimal = decimal*2 + int(digit)
print('The binary Number :', binary)
print('The decimal Number :', decimal)