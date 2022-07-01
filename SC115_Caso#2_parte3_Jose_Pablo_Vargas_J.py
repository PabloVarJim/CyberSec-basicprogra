#Welcome to student
print("\n\tWelcome to the school “Estrellita feliz”, we will check if you provide a natural number.")
#Ask to the student to enter a number and validate if it is a natural number.
for i in range (1,100000000000):
    num1 = int(input("Provide a natural number: "))
    if num1 > 0:
        print("\nCongratulations the number", num1, "is a natural number")
    if num1 < 0:
        print("\n","ERROR!!, the number provided is not a natural number")
    else:
        print()
        break
print("\tThank you for learning with us")