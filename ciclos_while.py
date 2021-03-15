# -*- coding: utf-8 -*-

def suma_n(n):
    "Suma los números de 1 a n"
    result = 0
    x = n
    while x > 0:
        result += x
        x -= 1
    return result


suma_n(7)


def ciclo_infinito():
    "Imprime el número 1 infinitas veces"
    i = 1
    while i <= 10:
        print(i, end=" ")


ciclo_infinito()
