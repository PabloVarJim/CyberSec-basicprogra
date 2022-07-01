#solicita la nota 
nota = int (input("Ingrese su nota: "))
if nota >= 90:
	print ("Aprobado y destacado") 
elif nota >= 70:
    print("Aprobado")
elif nota >= 60:
    print("Aplazado")
else:
    print("Reprobado ")
print("Nos vemos...!")