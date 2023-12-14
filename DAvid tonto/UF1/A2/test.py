def menu():
    print('''
    1 DoubleMe
    2 CalculateDiscount
    3
    4
    ''')


def uno():
    valor = float(input("valor: "))
    print(valor * 2)

def dos():
    original = float(input("Introduce el precio original: "))
    actual = float(input("Preu actual:"))
    porcentaje = ((original - actual) / original) * 100
    print("Has tenido un descuento del: ",porcentaje,"%" )

def tres():
    pi = float(3.14)
    pizzadiam = float(input("Cual es el diametro en cm de la pizza?: "))
    radio = pizzadiam / 2
    area = pi * radio ** 2
    print("Tu pizza tiene una area de",area,"cm²")

menu()