CAP= "  \...../"
ULLS= "   ╚⊙ ⊙╝"
COS = "  ═(███)═"
COS1 = "   ═(███)═"
COS2 = " ═(███)═"
CUA =  "    ═V═"

def serie():
    print(COS)
    print(COS1)
    print(COS)
    print(COS2)

largo = 0

try:
    while largo < 5:
        largo = int(input("Cuanto quieres que mida?, tiene que ser mas de 5: "))

    print(CAP)
    print(ULLS)

    for x in range(largo):
        serie()


    print(CUA)
except ValueError:
    print("Error!!!!!!")