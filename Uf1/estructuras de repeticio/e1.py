"""
Pol Danes - Yeray Lopez - David Muñoz
Asixc1B

Programa que demana a l'usuari la introducció de 10 nombres sencers (que també podrien ser 10000000 😱😳😈) i ha de mostrar, al final i per pantalla, quants són positius, quants negatius i quants zero.
"""
num_pos = 0
num_neg = 0
num_zero = 0
try:
    for i in range (10):
        numero = int(input("Pon un numerito entero: "))
        if numero < 0:
            num_neg += 1
        elif numero > 0:
            num_pos += 1
        else:
            num_zero += 1
    print("postivo: ",num_pos)
    print("negativos: ", num_neg)
    print("zeros: ",num_zero)

except ValueError:
    print("Asi no bobo")









