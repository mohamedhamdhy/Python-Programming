# 15. A certain grade of steel is graded according to the following conditions:
# Hardness must be greater than 50
# Carbon content must be less than 0.7
# Tensile strength must be greater than 5600
# The grades are as follows:

# Grade is 10 if all three conditions are met
# Grade is 9 if conditions (i) and (ii) are met
# Grade is 8 if conditions (ii) and (iii) are met
# Grade is 7 if conditions (i) and (iii) are met
# Grade is 6 if only one condition is met
# Grade is 5 if none of the conditions are met
# Write a program, which will require the user to give values of hardness, carbon content and tensile strength of the steel under consideration and output the grade of the steel.

"""
    hs = Hardness of steel
    cc = Carbon content
    ts = Tensile strength
    """
hs_f=0
cc_f=0
ts_f=0
hs = float(input("Enter the value of Hardness : "))
cc = float(input("Enter the value of Carbon Content: "))
ts = float(input("Enter the value of Tensile Strength: "))
if (hs>50):
	hs_f=1
if (cc<0.7):
	cc_f=1
if (ts>5600):
	ts_f=1
if(hs_f==0 and cc_f==0 and ts_f==0):
	grade = 5
elif(hs_f==1 or cc_f==1 or ts==1):
	grade = 6
elif(hs_f==1 and cc_f==0 and ts_f==1):
	grade = 7
elif(hs_f==0 and cc_f==1 and ts_f==1):
	grade = 8
elif(hs_f==1 and cc_f==1 and ts_f==0):
	grade = 9
#elif(hs_f==1 and cc_f==1 and ts_f==1):
else:
	grade = 10
 
print("The Grade of Steel  :", grade)