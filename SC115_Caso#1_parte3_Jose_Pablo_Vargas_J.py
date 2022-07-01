#Welcome to student
print("\n\tWelcome to the school “Estrellita feliz”, we will learn which numbers are odd or even.")
def pregunta():
    a = int(input("\nEnter the first number: "))
    b = int(input("\nEnter the second number: "))
    #Check if a is higher or lower than b, if lower show an error message and restart
    if a < b:
        print("ERROR, first number must be higher than second number")
        pregunta()
    elif a > b:
        if a % 2 == 0:
            print("\nThe number", a, "is even")
        if a % 2 != 0:
            print("\nThe number", a, "is odd")
        if b % 2 == 0:
            print("\nThe number", b, "is even")
        if b % 2 != 0:
            print("\nThe number", b, "is odd")
    else:
        print()
    print("\n\tCongratulations, you learned what numbers are odd or even.")
pregunta()