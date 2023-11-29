''''
Pol Danes - Yeray Lopez - David Muñoz
Asixc1B

Programa que mostra per pantalla la suma de tots els nombres senars i de tots els nombres parells inferiors a un número límit, que l’usuari introdueix per teclat.
'''

numlimit = int(input("Introdueix un numero limit: "))
numero = 0

numsenar = 0
sumasenar = 0

numparell = 0
sumaparell = 0

for x in range(numlimit):
    numero += 1
    if numero % 2 != 0:
        numsenar += 1
        sumasenar = sumasenar + numsenar
    else:
        numparell += 1
        sumaparell += sumaparell

print(sumaparell)
print(sumasenar)

