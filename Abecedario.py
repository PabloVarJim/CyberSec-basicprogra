v = ""
c =""
while v == "a,e,i,o,u" or "A,E,I,O,U":
    c != v
    letra = (input("Ingrese una letra: "))
    if letra == v:
        print("Ingresaste una vocal")
    elif letra == c:
        print("Ingresaste una consonante")