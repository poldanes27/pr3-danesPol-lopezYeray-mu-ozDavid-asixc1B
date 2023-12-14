'''
David Muñoz Anastasio
05/10/2023
M03 UF1
Calcula quants € tens
'''
print("Cuantas monedas tienes?")
euro2 = int(input("2€: "))
euro1 = int(input("1€: "))
euro05 = int(input("0.50€: "))
euro020 = int(input("0.20€: "))
euro010 = int(input("0.10€: "))
euro005 = int(input("0.05€: "))

euro2f = euro2 * float(2.00)
euro1f = euro1 * float (1.00)
euro05f = euro05 * float (0.5)
euro020f = euro020 * float (0.20)
euro010f = euro010 * float (0.10)
euro005f = euro005 * float (0.05)

suma_euros = (euro2f + euro1f + euro05f + euro020f + euro010f + euro005f)
print("Tienes un total de", suma_euros,"€")