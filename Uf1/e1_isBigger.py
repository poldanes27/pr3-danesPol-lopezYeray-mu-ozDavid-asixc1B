"""
Pol Danes - Yeray Lopez - David Muñoz
Asixc1B

Programa que demana dos números si el primer és més gran o igual que el segon els intercanvia. I torna a mostrar els valors per pantalla

"""

num1 = int(input("Possa un numero: "))
num2 = int(input("Possa un numero: "))
temp = 0

if num1 >= num2:
    temp = num1
    num1 = num2
    num2 = temp

    print (num1, num2)
else:
    print ("el primer numero no es mes gran q el segon")


