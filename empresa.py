cost = int(input("\nPlease enter the cost of your item: "))
meses = int(input("\nPlease enter the amount of months required to pay the item: "))
print("\t\nhe subtotal of your purchase is: "),cost
interest = cost*0.02
print("\t\nThe interest per month will be = ",interest)
fee = cost / meses + interest
print("\t\n The fee including interest will be =", fee)
pending = cost - fee
print("\t\n Your pending balance is= ",pending)
for x in range(meses):
    balance1 = pending - fee
    print("\t\n Your pending balance is= ",balance1)
    balance2 = balance1 - fee
    print("\t\n Your pending balance is= ",balance2)
    balance3 = balance2 - fee
    print("\t\n Your pending balance is= ",balance3)
    if x < 0:
        print("You cancelled your debt.")
    break
print("\nThanks for your purchase.")