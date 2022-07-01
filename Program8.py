#This program will calculate your salary, after requesting the amount of hours worked and hourly rate then applying deductions.

#Ask user to enter the amount of hours worked per week and hourly rate 

num1= int(input("Provide the total amount of hours worked: "))
num2= int(input("Provide your hourly rate : "))

Weekly_salary= (num1*num2)

#Social security (10.5%) and Insurance deductions(5%)

Deductions=84.5
Salary_deductions= Weekly_salary*(Deductions / 100)
Total_salary= Salary_deductions * 4.2

print("Your total salary after deductions will be:",Total_salary,)
