# fib(n) = fib(n-1) + fib(n-2) Con fib(0) = 0 y fib(1) = 1
# Programar esta función y evaluarla en 35. ¿Qué valor devuelve?

def Fibonacci(n):
    if n < 0:
        print("Número incorrecto")
    # El primer número de Fibonacci es 0
    elif n == 0:
        return 0
    # El segundo número de Fibonacci es 1
    elif n == 1:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)


print(Fibonacci(35))
