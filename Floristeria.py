precio=0
IVA=0
producto= ""
Total_producto=0
Total_factura=0
Total_final=0
num_linea=1
linea1 = ""
linea2 = ""
linea3 = ""
linea4 = ""

#saludo
print("BIENVENIDO A LA FLORISTERIA /n")

opcion= str(input("Desea ingresar una factura?, digite S o s :"))

#ingresar la factura

while opcion == "S" or opcion == "s":
    print("\nNuestras flores disponibles son las siguientes:")
    print("\t1. Rosas rojas")
    print("\t2. Rosas blancas")
    print("\t3. Claveles")
    print("\t4. Rosas orquideas")

    tipo= int(input("Digite el número correspondiente al tipo de flor que desea: "))

    cantidad= int(input("Digite la cantidad de flores:"))
    if tipo == 1:
        precio=100
        producto="Rosas rojas"
    elif tipo == 2:
        precio=150
        producto="Rosas blancas"
    elif tipo == 3:
        precio=75
        producto="Claveles"
    elif tipo == 4:
        precio=150
        producto="Orquideas"
    else:
        print("Ese tipo de flor no existe")

#operacion matemática
    Total_producto = precio * cantidad 
    Total_factura += Total_producto

#Concatena en una variable literal producto, la cantidad y total de producto 

    if num_linea == 1:
        linea1 = producto + "\t" + str(cantidad) + "\t\t" + str(Total_producto)
    elif num_linea == 2:
        linea2 = producto + "\t" + str(cantidad) + "\t\t" + str(Total_producto)
    elif num_linea == 3:
        linea3 = producto + "\t" + str(cantidad) + "\t\t" + str(Total_producto)
    elif num_linea == 4:
        linea4 = producto + "\t" + str(cantidad) + "\t\t" + str(Total_producto)
    num_linea += 1
    if num_linea<= 4:
        opcion= str(input("Desea ingresar un nuevo producto?, S o s :"))
    else:
        opcion= "n"

#Calculo de IVA y Total final
IVA= Total_factura*0.13
Total_final= Total_factura + IVA

#Imprimir factura
print("\nFactura de pago de Floristeria La Hermosa")
print("\nProducto   Cantidad    Precio Total")
print(linea1)
print(linea2)
print(linea3)
print(linea4)
print("\nEl monto total de los productos es: ", Total_factura)
print("\nEl monto del IVA es: ", IVA)
print("\nEl monto total con IVA es: ", Total_final)
print("Gracias por su compra")