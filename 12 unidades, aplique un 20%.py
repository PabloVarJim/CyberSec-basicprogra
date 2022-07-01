#solicita el precio y luego se convierte en un entero 
precio = input("Ingrese el precio del producto: ")
precio = int(precio)

#solicita la cantidad y se utiliza la función en la misma línea 
cantidad = int(input("Ingrese la cantidad: "))
if cantidad >= 12:
    #si la cantidad es al menos 12 
    # se hace un rebajo del 20%
    precio = precio * 0.8
#Se obtiene el valar total de la compra
total = precio * cantidad 
#Se muestra el valor al usuario 
print ("El total a pagar es: ",total) 