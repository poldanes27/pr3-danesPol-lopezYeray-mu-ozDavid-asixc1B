try:
    numero = int(input("Numero: "))
    for fila in range(numero):
        for x in range(fila+1):
            print("#", end="")
        print("")
except ValueError:
    print("Numero incorrecto")