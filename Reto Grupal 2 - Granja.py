#determinar el precio de venta por cada kilo de huevos.
#determinar el promedio de calidad de la gallina.
#formula promedio calidad = peso de gallina(k) * altura de gallina (cm) / número de huevos

#Saludo
print("Bienvenidos a la granja Los Huevos de Oro")
while True:
    print("Opción 1 - Cálculo de precio")
    print("Opción 2 - finalizar programa")
    opción = int(input("Opción elegida: "))
    if opción == 1:
        print("Por favor ingrese la informacion necesaria abajo:")
        ps = int(input("Ingrese peso de la gallina: "))
        al = int(input("Ingrese altura de la gallina en centímetros: "))
        nh = int(input("Ingrese numero de huevos de la gallina: "))
        pc = ps * al / nh
        print("El promedio caludad de la gallina es: ",pc)
    elif pc >= 15:
        pc1 = 1.2*pc
    elif pc > 8 and pc < 15:
        pc2 = 1*pc
    elif pc >=8:
        pc3 = 0.80 * pc
    
    
    elif opción == 2:
        print("Hasta la próxima")
        break
    else:
        print("Opción incorrecta. Debe ingresar 1 o 2")