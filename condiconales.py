# EJERCICIO CONDICIONAL
# Definir la variable x = 1+4*3+8/2*4+5**2
# Si el x es par sumarle 1 a x. Y si es impar sumarle 2
# ¿Que valor tiene x?
x = 1 + 4 * 3 + 8 / 2 * 4 + 5 ** 2
if x % 2 == 0:
    print("Es par y el valor de x es ", x + 1)
else:
    print("Es impar y el valor de x es ", x + 2)
