#User will be asked to provide the age of 5 different people

print ("We will calculate the average age of a group of 5 people")
print("Please provide the age of each person below: ")

age1 = float (input("Provide the age of person A: "))
age2 = float (input("Provide the age of person B: "))
age3 = float (input("Provide the age of person C: "))
age4 = float (input("Provide the age of person C: "))
age5 = float (input("Provide the age of person E: "))

average = (age1+age2+age3+age4+age5) / 5
print("The average age of the group is: ", average)
