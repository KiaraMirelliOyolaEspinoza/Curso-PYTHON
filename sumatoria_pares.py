# ¿Cuál es el resultado de sumar los primeros 50 números pares?
# (Desde el 2 inclusive hasta el 100 inclusive).

def suma_pares():
    acumulador = 0
    for i in range(2, 101, 2):
        acumulador = acumulador + i
    print(acumulador)


suma_pares()
