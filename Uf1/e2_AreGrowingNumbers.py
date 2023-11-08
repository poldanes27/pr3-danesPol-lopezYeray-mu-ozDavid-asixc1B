"""
Pol Danes - Yeray Lopez - David Muñoz
Asixc1B

Programa que detecta si tres números demanats han estat introduïts en ordre creixent.

"""

num1 = int(input("Possa un numero: "))
num2 = int(input("Possa un numero: "))
num3 = int(input("Possa un numero: "))

if num1<=num2 and num2<=num3:
    print("Els numeros ha sigut introduits de forma creixent: ")
else:
    print("Els numeros no han sigut introduits de forma creixent :( ")