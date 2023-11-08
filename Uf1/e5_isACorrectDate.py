"""
Pol Danes - Yeray Lopez - David Muñoz
Asixc1B

Programa que comprovi si una data és correcte. El programa ha de demanar una data, dia, mes i any (en el format DD/MM/AAAA).  Cal recordar que hi ha anys de traspàs. NO es pot fer servir funcions de calendari com ara datetime de Python.
"""

data = input("Possa el dia mes i any en format DD/MM/AAAA").split("/")
dia = int(data[0])
mes = int(data[1])
año = int(data[2])

if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 11:
    print("31 dies")

elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
    print("30 dies")

elif mes == 2:
    print("te 29 o 28 dies")

else:
    print("Eres tonto")
"""
numero = input("")
match numero:
    case "1" | "3" | "5" | "7" | "8" | "10" | "11" |:print ("31")
    case "4 "| "6" | "9" | "11":print("30")
    case "2": print("28")
    case _: print ("Mes no valid")
"""