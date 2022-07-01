#This program calculate the salary of a person, after requesting the amount of hours worked and hourly rate

#Ask user to enter the amount of hours worked per week

hourly_wage = float(input("Provide your hourly wage: "))
hours_worked = float(input("Provide the total amount of hours worked: "))
print("Your monthly Salary is: ")
monthly_salary = print(hourly_wage * hours_worked * 4.2)

#Social security (10.5%) and Insurance deductions(5%)
