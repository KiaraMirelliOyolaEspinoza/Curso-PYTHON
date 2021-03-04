# -*- coding:utf-8 -*-

def peso(masa, gravedad=9.8):
    "Fórmula del peso"
    return masa * gravedad


# Ingresamos parámetros opcionales
print("Peso en la tierra:", peso(10))
print("Peso en la luna:", peso(10, 1.36))

# Ingresamos parámetros con palabras claves o argumentos nombrados
print("Peso den la luna:", peso(10, gravedad=1.63))
print("Peso de la luna:", peso(masa=10, gravedad=1.63))
print("Peso de la luna:", peso(gravedad=13.5, masa=10))

# Lista de parámetros


def suma_numeros(*args):
    "Suma de los números que pasaremos como parámetros"
    return sum(args)


print("2+3+4 =", suma_numeros(*[2, 3, 4]))
print("2+3+4 =", suma_numeros(2, 3, 4))

# Diccionario de parámetros


def imprimir_ticket(*args, **kwargs):
    "Imprime el ticket de una compra"
    print("Detalle ticket")
    for item, precio in kwargs.item():
        print(item, ";", precio)
