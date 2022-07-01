#this summary function is used to create final booking report
def summary():
    print("Please find the summary of your next adventure with El Paraise below")
    print()
    print("The total amout to pay is: ")
    #print((a*5000)+(b*2500)+(c*7000)+(d*3500))
    print()
def tickets_required():
    print()
    print("Please select the amount of tickets required, remember each Sky Tram has a maximum occupancy of 6 passengers")
    print()
    print("1. Cantidad de Nacionales adultos. Precio por ticket 5000 colones")
    print()
    print("2. Cantidad de Nacionales adultos mayores o ninos. Precio por ticket 2500 colones")
    print()
    print("3. Cantidad de Extrangeros adultos. Precio por ticket 7000 colones")
    print()
    print("3. Cantidad de Extrangeros adultos mayores o ninos. Precio por ticket 3500 colones")
    print()
    a = int(input("Ingrese la cantidad de nacionales adultos: "))
    print()
    b = int(input("Ingrese la cantidad de nacionales adultos mayores o ninos: "))
    print()
    c = int(input("Ingrese la cantidad de extrangeros adultos: "))
    print()
    d = int(input("Ingrese la cantidad de extrangeros adultos mayores o ninos: "))
    print()
    tickets_amount = print("The total amount of tickest purchased is:",(a+b+c+d))
    if (a+b+c+d)>6:
         print("ERROR, the maximum occupancy is 6")
    summary()

# this function is used to define the time our tours are available
def tour_hour():
    print()
    print("At time would you like to enjoy of the tour? ")
    print()
    print("1. 8:00 am")
    print("2. 10:00 am")
    print("3. 12:00 md")
    print("4. 2:00 pm")
    print()
    a = int(input("Please choose a time for your tour: "))
    tickets_required()
    return 0
 
# this function is used to select tour view
def tour_view():
    print("Select one of our wonderful views below: ")
    print()
    print("1. Rio Celeste view")
    print("2. Waterfalls view")
    print("3. Ocean view")
    print()
    tour = int(input("Choose the tour you'd like to enjoy: "))
    if tour == 1:
      tour_hour()
    elif tour == 2:
      tour_hour()
    elif tour == 3:
      tour_hour()
    else:
      print("wrong choice, please select 1, 2 or 3.")
      print()
tour_view() # it calls the function tour_hour