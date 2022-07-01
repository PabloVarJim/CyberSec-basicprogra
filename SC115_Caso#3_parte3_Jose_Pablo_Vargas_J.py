#Welcome to student
print("\n\tWelcome to the school “Estrellita feliz”, we will check if you to enter the correct answer.")
print()
num1 = int(input("Please enter any number equal or lower to 100: "))
if num1 >= 101:
    print("\nERROR! The number entered is higher than 100, please try again.")
elif num1 <= 100:
    print("\nCongratulations, you answer is correct.")
else:
    print()
print("\n\tThank you for learning with us.")