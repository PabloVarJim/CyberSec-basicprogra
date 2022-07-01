#Calculation of the Perimeter and Area of a square

print("We will calculate the Perimeter and Area of a square using the size of one side")

print("Please provide the size of 1 side of the square")

Side_size = int(input("Size of one side: "))

#The perimeter of a square is given by the formula, Perimeter = 4 x side.

perimeter = Side_size + Side_size + Side_size + Side_size
print("The Perimeter of the square is: ",perimeter)

#The area of a square is given by the formula, Area of a Square = side × side = side².

area = Side_size*Side_size
print("The Area of the rectangle is: ",area)
