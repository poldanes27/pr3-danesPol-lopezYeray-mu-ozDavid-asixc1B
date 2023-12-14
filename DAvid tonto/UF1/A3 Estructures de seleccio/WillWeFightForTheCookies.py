'''
David Muñoz Anastasio
25/10/2023
M03 UF1
Repartir galetes
'''
try:
    persones = int(input("Quantes persones?: "))
    galetes = int(input("Quantes galetes?: "))
    if (galetes % persones) != 0:
        print("Let's Fight")
    else:
        print("Let's Eat")
except ValueError:
    print("Error, posa nomes numeros enters")