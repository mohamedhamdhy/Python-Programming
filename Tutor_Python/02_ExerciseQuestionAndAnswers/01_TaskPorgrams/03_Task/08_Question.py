# 08. Write a program to find the decimal number from given Binary number

"""
def convertToBinary(n):
   if n > 1:
       convertToBinary(n//2)
   print(n % 2,end ="")
 
decimal = int(input("Enter the Decimal Number :"))
convertToBinary(decimal)
 
 
"""
decimal = int(input("Enter the Decimal Number :"))
binary = 0
ctr = 0
temp = decimal
while(temp > 0):
    binary = ((temp%2)*(10**ctr)) + binary
    temp = int(temp/2)
    ctr += 1
print("Decimal Number :",decimal)
print("Binary Number :",binary)