#Sistema de reservaciones para Telefericos Aventuras "El Paraíso".
#Booking system for Sky Trams Aventuras "El Paraíso".

#Mensaje de bienvenida para nacionales

print("BIENVENIDOS - WELCOME <BANNER>")
print()
print("Bienvidos a Aventuras “El Paraíso”, donde podrás disfrutar de la mejor vista de la naturaleza desde las alturas.")
print()

#Mensaje de bienvenida para extranjeros
print("Welcome to Adventures “El Paraiso”, enjoy the best view of nature from the heights.")
print()
print("Servicios - Services")
print()

#Descripcion de los servicios en español
print("Nuestros servicios ofrecen 3 teleféricos en diferentes áreas de Costa Rica donde podrás disfrutar de la naturaleza nacional única. Cada teleférico tiene un espacio máximo de 6 personas, en 4 horarios diarios diferentes (8AM, 10AM, 12MD y 2PM).")
print()

#Descripcion de los servicios en inglés
print("Our services include 3 Sky Trams in different locations throughout Costa Rica, where you will be able to enjoy our unique national nature. Each Sky Tram has a maximum occupancy of 6 people, with 4 different times during the day (8AM, 10AM, 12MD y 2PM).")
print()
print("Regulaciones - Regulations")
print()

#Regulaciones
print("Regulaciones del servicio: Edad mínima 9 años, buen estado de salud y un peso máximo 160 kg, 352 lbs.")
print()

#Regulations
print("Service regulations: Minimum age 9 years old, good health conditions required and maximum weight supported 160kg, 352lbs.")
print()

#Tipos de vistas
tour1 = ("Rio Celeste view")
tour2 = ("Waterfalls view")
tour3 = ("Ocean view")

#Tipos de tickets
nacionales_adultos = (5000)
nacionales_ninos_mayores = (2500)
extranjeros_adultos = (70000)
extranjero_ninos_mayores = (35000)

#Horarios disponibles
horario1 = ("8:00 am")
horario2 = ("10:00 am")
horario3 = ("12:00 md")
horario4 = ("2:00 pm")

# This function is used to select tour view
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
    tour_hour()
# this function is used to define the tour_hour
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
#this tickets_required is used to define the amoun of tickets per reservation
def tickets_required():
    print()
    print("Please select the amount of tickets required, remember each Sky Tram has a maximum occupancy of 6 passengers")
    print()
    print("1. Cantidad de Nacionales adultos. Precio por ticket 5000 colones")
    print()
    print("2. Cantidad de Nacionales adultos mayores o niños. Precio por ticket 2500 colones")
    print()
    print("3. Cantidad de Extranjeros adultos. Precio por ticket 7000 colones")
    print()
    print("3. Cantidad de Extranjeros adultos mayores o niños. Precio por ticket 3500 colones")
    print()
    a = int(input("Ingrese la cantidad de nacionales adultos: "))
    print()
    b = int(input("Ingrese la cantidad de nacionales adultos mayores o niños: "))
    print()
    c = int(input("Ingrese la cantidad de Extranjeros adultos: "))
    print()
    d = int(input("Ingrese la cantidad de Extranjeros adultos mayores o niños: "))
    print()
    tickets_amount = print("The total amount of tickets purchased is:",(a+b+c+d))
    if (a+b+c+d)>6:
         print("ERROR, the maximum occupancy is 6")
         return tickets_required()
    summary()
#this summary function is used to create final booking report
def summary():
    print("Please find the summary of your next adventure with El Paraiso below")
    print()
    print("The total amount to pay is: ")
    print()
    print("Thank you for choosing our services, enjoy of this wonderful experience with Adventures “El Paraiso")
    return 0
tour_view()