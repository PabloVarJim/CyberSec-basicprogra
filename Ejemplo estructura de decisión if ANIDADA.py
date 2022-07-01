#solicita la nota 
nota = int (input("Ingrese su nota: "))
if nota >= 70:
	print ("Aprobado") 
else:
    if nota >= 60:
        print("Aplazado")
    else:
        print("Reprobado ")
print("Nos vemos...!")