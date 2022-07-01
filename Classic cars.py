antiguedad=0
contador=0
product=""
#Solicitar el anio de 10 vehiculos
for i in range(10):
    modelo = int(input("Ingrese el anio de fabricacion de su vehiculo: "))
    antiguedad = (2022-modelo)
    if antiguedad >= 30:
        contador +=1
#Mostrar resultado
print("La cantidad de autos clasicos es: ", contador)