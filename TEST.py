#Request to the user all the information required for each of the items/products

item1_name = input("Please enter the name of item #1: ")
item1_price = float(input("Please enter the price of item #1: "))
item1_quantity = float(input("Please enter the quantity of item #1: "))

print()

item2_name = input("Please enter the name of item #2: ")
item2_price = float(input("Please enter the price of item #2: "))
item2_quantity = float(input("Please enter the quantity of item #2: "))

print()

item3_name = input("Please enter the name of item #3: ")
item3_price = float(input("Please enter the price of item #3: "))
item3_quantity = float(input("Please enter the quantity of item #3: "))

print()

#Calculate the subtotal of item #1

item1_subtotal = (item1_price*item1_quantity)
print(("Subtotal of item #1: ",item1_subtotal))

print()

#Calculate the subtotal of item #2

item2_subtotal = (item2_price*item2_quantity)
print(("Subtotal of item #2: ",item2_subtotal))

print()

#Calculate the subtotal of item #3

item3_subtotal = (item3_price*item3_quantity)
print(("Subtotal of item #3: ",item3_subtotal))

print()

#Calculate the subtotal of all items/products

sub_total = item1_subtotal+item2_subtotal+item3_subtotal
print ("Subtotal is: ",(sub_total))

print()

#10% Discount on purchase

Discount = (sub_total*10/100)
print(("The 10% discount is: "),Discount)
price_discount = (sub_total-Discount)
print(("Subtotal with discount is: "),price_discount)

print()

#Calculate the 13% taxes after discount

Taxes = (price_discount*13/100)
Total = (price_discount-Taxes)
print(("The taxes for the total amount is: "),Taxes)

print()

#Calculate the total after discount and taxes

Total = (price_discount+Taxes)
print(("The total amount to pay is :",Total))

print()

#SUMMARY TABLE
from tabulate import tabulate
data = ["1", "item1_name", "item1_quantity", "item1_subtotal"]
print (tabulate(data, headers=["Item #", "Product", "Quantity", "Subotal"]))









