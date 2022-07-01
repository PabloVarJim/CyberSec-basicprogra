quien= "Minor"
i=0
while i < 3:
	i = i+1
	nombre=input("Cual es su nombre?") 
	if quien != nombre:
		print("No eres Minor")
	else:
		print("Bienvenido Minor")
		break
else:
	print("Se excedió el número de intentos")
