'''
David Muñoz Anastasio
19/10/2023
PP1 UF1
Calcular diagonal
'''
try:
    # Preguntar les mesures
    amplada = int(input("Quina es l'amplada en metres?: "))
    alcada = int(input("Quina es l'alçada en metres?: "))

    # no recordo com era l'arrel :(
    diagonal = ((amplada ** 2)+(alcada ** 2))
    print("La diagonal mesura", diagonal, "m")
except ValueError:
    print("Nomes posa numeros")
