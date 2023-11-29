"""
Pol Danes - Yeray Lopez - David Muñoz
Asixc1B

Programa que mostra un triangle amb nombres a les cantonades.  Cal demanar quina alçada ha de tenir el triangle. Els valors permesos per a l'alçada son entre 2 i 9. (ambdós inclosos)
INPUT
Alçada del triangle: 5
OUTPUT
1
2 2
3   3
4     4
5 5 5 5 5
"""
try:
    valor = 0
    contador = -2
    espai = (" ")
    alçada = int(input("Quina es l'alçada del triangle: "))
    for i in range (alçada):
        valor += 1
        for x in range(i + 1):
            contador += 1
            if contador > 0:
                print(i,espai * i,i, end=" ")
            else:
                print(valor, end=" ")
        print()
except ValueError:
    print("Javi no lo rompas porfavor")