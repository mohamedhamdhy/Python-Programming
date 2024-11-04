# If the marks obtained by a student in five different subjects are input through the keyboard, find out the aggregate marks and percentage marks obtained by the student. Assume that the maximum marks that can be obtained by a student in each subject is 100.



m1=int(input("Enter the marks 1:"))
m2=int(input("Enter the mark 2:"))
m3=int(input("Enter the mark 3:"))
m4=int(input("Enter the mark 4:"))
m5=int(input("Enter the mark 5:"))
total=m1+m2+m3+m4+m5
per=total/5
print("Total Marks:",total)
print("Percentage Marks:",per)