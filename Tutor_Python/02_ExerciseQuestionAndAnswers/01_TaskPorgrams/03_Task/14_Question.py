# 14. Write a program to find the value of one number raised to the power of another

base = int(input("Enter the Base Number :"))
pow = int(input("Enter the Power Number :"))
#res=(base**pow)
#print("Answer :",res)
res = 1
while pow != 0:
    res *= base
    pow-=1
 
print("Answer :",res)