# 05. A company insures its drivers in the following cases:

# If the driver is married.
# If the driver is unmarried, male & above 30 years of age.
# If the driver is unmarried, female & above 25 years of age.

age = int(input("Enter the Age :"))
sex = input("Enter the Gender M/F :")
status = input("Enter the Marital Status U/M :")
if( status == 'M' or status == 'm'):
	print( "Driver should be Insured" )
elif( status == 'U' and sex == 'M' and age > 30 or status == 'u' and sex == 'm' and age > 30 ):
	print( "Driver should be Insured" )
elif( status == 'U' and sex == 'F' and age > 25 or status == 'u' and sex == 'f' and age > 25 ):
	print( "Driver should be Insured" )
else:
	print( "Driver should not be Insured" )
"""
age = int(input("Enter the Age :"))
sex = input("Enter the Gender M/F :")
status = input("Enter the Marital Status U/M :")
if ( ( status == 'M') or ( status == 'U' and sex == 'M' and age > 30 ) or( status == 'U' and sex == 'F' and age > 25 ) ):
	print( "Driver should be Insured" )
else:
	print( "Driver should not be Insured" )
 
"""