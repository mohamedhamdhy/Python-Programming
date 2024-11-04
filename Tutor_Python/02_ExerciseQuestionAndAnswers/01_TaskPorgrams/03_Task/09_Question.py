# 09. Write a program to find the factorial of the given number


f = int(input("Enter the Number :"))
fact = 1    
if(f< 0):    
   print("Factorial does not exist Negative Values")    
elif(f== 0):    
   print("The Factorial of 0 is 1")    
else:    
   for i in range(1,f + 1):    
       fact = fact*i    
   print("The Factorial",f,"is :",fact)  