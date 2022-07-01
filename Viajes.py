#variables y constantes
destino1 = 10000
destino2 = 12000
destino3 = 25000
destino4 = 13000

#Inicio del programa de bienvenida
print("\nBIENVENIDOS A DESTINOS")
print("\nA contuniacion se le detallan los viajes disponibles: ")
print()
print("\t1. Cancun:         $10000")
print("\t2. Punta Cana:     $10000")
print("\t3. Las Vegas:      $10000")
print("\t4. Orlando:        $10000")
print()
#Solicite al usuario el destino
destino=int(input("Escoga una de las opciones descritas anteriormente (1 a 4): "))
while(destino==1 or destino==2 or destino==3 or destino==4):
    break
else:
    destino=int(input("Su opcion no es valida, debe escoger una opcion entre 1 a 4."))
print()
#Cantidad de cuotas
print("\nIngrese la cantidad de cuotas en las que va a pagar el viaje: ")
print("\nContamos con los siguientes planes:")
print("3 cuotas - Recargo de 5%")
print("6 cuotas - Recargo de 10%")
print("12 cuotas - Recargo de 15%")
print()
cuotas=(int(input("Digite 3, 6, 12, segun el plan que desea: ")))
#Realizar operaciones

#opcion destino #1
if destino == 1:
    destinofinal = "Cancun"
    montoInicial = destino1
    if cuotas==3:
        montoRecargo = destino1 * 0.05
        cuotaFinal = (montoRecargo + destino1)/3
    if cuotas==6:
        montoRecargo = destino1 * 0.10
        cuotaFinal = (montoRecargo + destino1)/6
    if cuotas==12:
        montoRecargo = destino1 * 0.15
        cuotaFinal = (montoRecargo + destino1)/12    
    else:
        print("Opcion invalida")

#opcion destino #2
elif destino == 2:
    destinofinal = "Punta Cana"
    montoInicial = destino2
    if cuotas==3:
        montoRecargo = destino2 * 0.05
        cuotaFinal = (montoRecargo + destino2)/3
    if cuotas==6:
        montoRecargo = destino2 * 0.10
        cuotaFinal = (montoRecargo + destino2)/6
    if cuotas==12:
        montoRecargo = destino2 * 0.15
        cuotaFinal = (montoRecargo + destino2)/12    
    else:
        print("Opcion invalida")

#opcion destino #3
elif destino == 3:
    destinofinal = "Las Vegasa"
    montoInicial = destino3
    if cuotas==3:
        montoRecargo = destino3 * 0.05
        cuotaFinal = (montoRecargo + destino3)/3
    if cuotas==6:
        montoRecargo = destino3 * 0.10
        cuotaFinal = (montoRecargo + destino3)/6
    if cuotas==12:
        montoRecargo = destino3 * 0.15
        cuotaFinal = (montoRecargo + destino3)/12    
    else:
        print("Opcion invalida")

#opcion destino #4
elif destino == 4:
    destinofinal = "Orlando"
    montoInicial = destino4
    if cuotas==3:
        montoRecargo = destino4 * 0.05
        cuotaFinal = (montoRecargo + destino4)/3
    if cuotas==6:
        montoRecargo = destino4 * 0.10
        cuotaFinal = (montoRecargo + destino4)/6
    if cuotas==12:
        montoRecargo = destino4 * 0.15
        cuotaFinal = (montoRecargo + destino4)/12    
    else:
        print("Opcion invalida")
print()
#Imprimir informacion
print("\nEl destino escogido es: ", destinofinal)
print("\nEl monton original del valor del viaje es: $",montoInicial)
print("\nCantidad de cuotas: ", cuotas)
print("\n Recardo de acuerdo con las cuotas es: $", montoRecargo)
print("\nEl monton final a cancelar es: $",cuotaFinal)