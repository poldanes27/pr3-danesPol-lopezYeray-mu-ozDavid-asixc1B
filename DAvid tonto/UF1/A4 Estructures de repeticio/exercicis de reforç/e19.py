

menu = 0
while menu == 0:
    try:
        print(
        '''
        1. Literatura
        2. Cinema
        3. Música
        4. Videojocs
        5. Sortir
        '''
        )
        seleccion = int(input("Selecciona: "))

        if seleccion == 5:
           menu += 1
        elif seleccion == 1:
            print("Suggeriments")

        elif seleccion == 2:
            print("cinema!")
        elif seleccion == 3:
            print("musica")
        elif seleccion == 4:
            print("videojocs")
        else:
            print("Seleccion equivocada intenta de nuevo")

    except ValueError:
        print("Error")