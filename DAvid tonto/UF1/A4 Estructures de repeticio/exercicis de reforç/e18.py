import time
segundos = 0
minutos = 0
horas = 0

while True:
    segundos += 1
    if segundos == 60:
        segundos = 0
        minutos += 1

    if minutos == 60:
        minutos = 0
        horas += 1
    if horas == 24:
        segundos = 0
        minutos = 0
        horas = 0
    print(f"{horas:02}:{minutos:02}:{segundos:02}")
    time.sleep(1)