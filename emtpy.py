#Definir variables para modulo de reservas

#Tipos de vistas
tour1 = ("Vista a Rio Celeste, en San Carlos")
tour2 = ("Vista a las Cataras, en Heredia")
tour3 = ("Vista al Oceano, en Guanacaste")

#Tipos de tickets
Na1 = 5000
Na2 = 2500
Ex1 = 7000
Ex2 = 3500

#Horarios disponibles
H1 = ("8:00 am")
H2 = ("10:00 am")
H3 = ("12:00 md")
H4 = ("2:00 pm")

#Tipo de tickets y costo
def tickets():
    print("A continuación digite la cantidad de tickets necesarios:")
    print()
    N1 =  int(input("Digite la cantidad de adultos nacionales: "))
    print()
    N2 = int(input("Digite la cantidad de ninos o adultos mayores nacionales: "))
    print()
    E1 = int(input("Digite la cantidad de extranjeros adultos: "))
    print()
    E2 = int(input("Digite la cantidad de ninos o adultos mayores extranjeros : "))
    print()
    monto_total = (N1*Na1+N2*Na2+E1*Ex1+E2*Ex2)
    if (N1+N2+E1+E1)>6:
        print("ERROR, La capacidad maxima por teleferico es de 6 personas")
        return tickets()
    elif (N1+N2+E1+E1)<6:
        print()
        print("El costo total de los tickets es:",monto_total)
tickets()

#Seleccion del horario que el usuario quiere disfrutar
def horarios_disponibles():
    print()
    print("Seleccione el horario que gustaria disfrutar del tour:")
    print()
    print("1. 8:00 am")
    print("2. 10:00 am")
    print("3. 12:00 md")
    print("4. 2:00 pm")
    print()
    horario = int(input("Please choose a time for your tour: "))
    if horario == 1:
        print("Gracias, el horario de su tour sera:",H1)
    elif horario == 2:
        print("Gracias, el horario de su tour sera:",H2)
    elif horario == 3:
        print("Gracias, el horario de su tour sera:",H3)
    elif horario == 4:
        print("Gracias, el horario de su tour sera:",H4)
    else:
        print("ERROR, selecciono un horario incorrecto.")
    print()
horarios_disponibles()

#Seleccion del tour que el usuario desea
def tour():
    print()
    print("Seleccione la vista que quisiera disfrutar:")
    print()
    print("1. Vista a Rio Celeste, en San Carlos")
    print("2. Vista a las Cataras, en Heredia")
    print("3. Vista al Oceano, en Guanacaste")
    print()
    vista = int(input("Please choose a time for your tour: "))
    if vista == 1:
        print("Gracias, el tour elegido es: Teleferico #1",tour1)
    elif vista == 2:
        print("Gracias, el tour elegido es: Teleferico #2",tour2)
    elif vista == 3:
        print("Gracias, el tour elegido es: Teleferico #3",tour3)
    else:
        print("ERROR, selecciono una vista incorrecta.")
    print()
tour()
