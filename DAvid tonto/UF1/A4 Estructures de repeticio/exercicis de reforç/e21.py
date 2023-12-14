import random
num1 = 0
num2 = 100
tmp = 0
intentos = 0
rango = random.randint(num1,num2)
win = False
numero = 0
try:
    numero = int(input("Pon un numero del 1-100: "))
    while intentos < 10:
        intentos += 1
        tmp = random.randint(num1,num2)
        if tmp == numero:
            win = True
            break
        pregunta = int(input(f"Es mes gran que {tmp}?:\n si = 1 \n no = 2\n"))

        if pregunta == 1:
            num1 = tmp +1
        if pregunta == 2:
            num2 = tmp -1
    if win == True:
        print(f"He ganado y me sobran {10 - intentos} intentos")
    else:
        print("He perdido me he quedado sin intentos")

except ValueError:
    print("Error")