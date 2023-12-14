'''
David Muñoz Anastasio
19/10/2023
PP1 UF1
Calcular nota final
'''

#Un def per poder executar una secuencia de comandes facilment
def pedir():
    #global per poder fer servir la variable fora del def
    global notafinal
    ra1 = float(input("Quina es la teva nota de RA1?: "))
    ra2 = float(input("Quina es la teva nota de RA2?: "))
    notafinal = ((ra1/10)*3) + ((ra2/10)*7)

#En cas d'un valor que no es ni numero ni decimal que ho notifiqui
try:
    pedir()
    estudiant1 = notafinal
    print("Següent estudiant")
    pedir()
    estudiant2 = notafinal
    print("Següent estudiant")
    pedir()
    estudiant3 = notafinal

    print("La nota de l'estudiant 1 és:", estudiant1)
    print("La nota de l'estudiant 2 és:", estudiant2)
    print("La nota de l'estudiant 3 és:", estudiant3)
except ValueError:
        print("Caràcter incorrecte")