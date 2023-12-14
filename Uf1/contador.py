import random

aleatori = random.randint(1,100)
contador = 10
vegades = 0
try:
    while contador != 0:
        while aleatori != resposta:
            resposta = int(input("Escolleix un numero"))
            if resposta < aleatori:
                print ("El teu numero es mes petit que el numero demanat")
            elif resposta > aleatori:
                print ("El teu numero es mes gran que el numero demanat")
            contador = contador -1
            vegades = vegades +1
            print ("Et queden ", contador, "intents" )
    print("Aquest era el numero:", aleatori )
    print("Has utilitzat:", vegades)

except ValueError:
    print("NONO")