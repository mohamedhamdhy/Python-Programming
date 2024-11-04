# 1. Ramesh's basic salary is input through the keyboard. His dearness allowance is 40% of basic salary, and house rent allowance is 20% of basic salary. Write a program to calculate his gross salary.

# Program to calculate gross salary
try:
    # Input: basic salary from the user
    basic_salary = int(input("Enter the basic salary: "))
    
    # Calculate allowances
    da = 0.4 * basic_salary  # Dearness Allowance
    hra = 0.2 * basic_salary  # House Rent Allowance
    
    # Calculate gross salary
    gross_salary = basic_salary + da + hra
    
    # Output: gross salary
    print("Gross Salary =", gross_salary)
except ValueError:
    print("Please enter a valid integer for the salary.")
