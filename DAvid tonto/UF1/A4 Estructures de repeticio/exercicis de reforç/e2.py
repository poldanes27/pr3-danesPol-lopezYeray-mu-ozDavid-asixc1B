import random
aleatori = random.randint(1,100)
intents = 0
win = False
while intents != 10:
    intents += 1
    try:
        numero = int(input("Prueba un numero: "))
        if numero == aleatori:
            print("Felicidades has acertado el numero con",intents,"intentos")
            intents = 10
            win = True
        elif numero < aleatori:
            print("Mas grande",)

        elif numero > aleatori:
            print("Mas pequeño")
    except ValueError:
        print("ERROR, pon solo numeros enteros")
        intents -= 1

if win == False:
    print("Te has quedado sin intentos el numero era",aleatori)


