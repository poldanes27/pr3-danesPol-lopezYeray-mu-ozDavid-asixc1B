'''
David Muñoz Anastasio
21/09/2023
M03 UF1
Programa de pregunta d'edat
'''
try:
    #Preguntem quina edat
    edat=int(input("Quina edat tens?: "))

    #Si té més de 18 li posem que es major d'edat
    if edat >= 18:
        print("Ets major d'edat")
    #En cas de que no, posare que no es major d'edat
    else:
        print("Ets menor d'edat")

    #Si te més de 66 anys edat de jubilació,
    if edat >= 66:
        print("Hora de jubilar-se")

    print('''
      ================
    ||Codi finalitzat ||
      ================
    ''')
except ValueError:
    print("Valor incorrecte")