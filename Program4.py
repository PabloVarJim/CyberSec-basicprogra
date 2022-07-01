#User will be asked to provide a number and the squared and cubed of that number will be calculated

print("We will calculate the result of the squared and cubed of any number provided")

#The first calculation will be the squared of a number provided

def squared(num1):
    return num1 * num1

num1 = int(input("Please type a number to get the squared : "))

#Now that the number was provide and action define, the result will be displayed

print ("The squared of the number provided is: ", squared(num1))

print("We will calculate the result of the cubed of any number provided")

#The second calculation will be the cubed of a number provided

def cube(num1):
    return num1 * num1 * num1

num1 = int(input("Please type your number to get the cubed: "))

#Now that the number was provide and action define, the result will be displayed

print ("The cubed of the number provided is: ", cube(num1))
