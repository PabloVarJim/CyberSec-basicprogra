#User will be asked to assign a number to each letter

print("To resolved the formula please assign a number to Letter A and Letter B")
Letter_A = int(input("Please provide a number for letter A: "))
Letter_B = int(input("Please provide a number for letter B: "))
print ("The result of the formula is: ")

#The formula will be resolved based on the numbers provided by the user
print((Letter_A + Letter_B)**2/3)
