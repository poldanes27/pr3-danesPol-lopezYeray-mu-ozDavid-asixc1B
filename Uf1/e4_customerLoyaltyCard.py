"""
Pol Danes - Yeray Lopez - David Muñoz
Asixc1B

Programa que demana l'import d'una factura, amb iva inclòs. Calcula l'import amb descompte, en cas de tenir la targeta de client, tenint en compte els següents criteris:
Si l'import de la factura, és igual o superior a 100 €, se li aplica un descompte del 21%, en cas contrari no se li aplica cap descompte. El descompte es calcula al preu final,  i no a la “base imponible”. I després si li aplica l’IVA . Precio total = Base imponible * Tipo de IVA
Exemple de càlcul:
Descompte del 21%:	95,59 = 121 * 0,79
Preu amb IVA: 	115,66 = 95,59 * 1,21
Preu Total 121 €, aplicat descompte 115,66 €  “jo no sóc tonto?”
Exemple:
Preu Total 357€ , aplicat descompte  341,26€
"""
factura = int(input("Quin es l'import de la factura amb iva inclos? "))
targeta = input("Tens targeta client? [si]-[no]: ")
if targeta == "si" and factura >= 100:
     factura = 0.79*factura
     factura = factura + factura*0.21
     print (factura)

elif targeta == "no":
    print("No tens targeta no se aplica cap descompte ")
elif factura < 100:
    print("El preu no es mes gran que 100 euros")




