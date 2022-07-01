#Calculation of the Perimeter and Area of a rectangle

print("We will calculate the Perimeter and Area of a Rectangle using length and width provided")

print("Please provide the Length and Width of the rectangle below")

Length = int(input("Length : "))
Width = int(input("Width : "))

#The perimeter of a rectangle is given by the formula, Perimeter = 2l+2w , L = Length and W = Width.

perimeter = 2*(Length + Width)
print("The Perimeter of the rectangle is: ",perimeter)

#The area of a rectangle is given by the formula, A = L*W , L = Length and W = Width.

area = Length * Width
print("The Area of the rectangle is: ",area)
