#Calculate the percentage of the monthly food expenses and the percentage free from monthly salary.

Monthly_earnings = int(input("Enter your monthly earnings: "))
Food_Expense = int(input("Enter your monthly food expense: "))

Expense_cost = Food_Expense/Monthly_earnings
Food_Percentage = Expense_cost*100
Percentage_free = 100 - Food_Percentage

#Calculation of percentages of food expense and earnings free

print("The percentage of your monthly food expense is: ",Food_Percentage,"%")
print("The percentage free of your salary is: ",Percentage_free,"%")
