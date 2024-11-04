# Function Overriding
class Employee:
    def WorkingHrs(self):
        self.hrs = 50
 
    def printHrs(self):
        print("Total Working Hrs : ", self.hrs)
 
 
class Trainee(Employee):
    def WorkingHrs(self):
        self.hrs = 60
 
    def resetHrs(self):
        super().WorkingHrs()
 
 
employee = Employee()
employee.WorkingHrs()
employee.printHrs()
 
trainee=Trainee()
trainee.WorkingHrs()
trainee.printHrs()
# Reset Trainee Hrs
trainee.resetHrs()
trainee.printHrs()