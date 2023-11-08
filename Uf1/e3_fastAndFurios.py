"""
Pol Danes - Yeray Lopez - David Muñoz
Asixc1B

Volem un programa que calculi la velocitat instantània i la velocitat mitjana. Cal demanar velocitat inicial (m/s), l'acceleració (m/s2) i el temps. Si la velocitat instantània és inferior o igual a 0, has d'indicar que està parat i no pots calcular la velocitat mitjana.
velocitat instantània = velocitat inicial + acceleració * temps
velocitat mitjana = (velocitat inicial + velocitat instantània )/2

"""
import math
veloinicial = int(input("Quina es la velocitat inicial: "))
acceleracio = int(input("Quina es la acceleracio : "))
temps = int(input("Quin ha sigut al temps: "))
veloinst = veloinicial + acceleracio * temps
if veloinst <= 0:
    print("Esta parat i no es pot calcular la velocitat mitjana")



