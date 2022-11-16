"""Ejercicio 2.1
Definir una función max() que tome como argumento dos números y devuelva el mayor
de ellos. (Es cierto que python tiene una función max() incorporada, pero hacerla
nosotros mismos es un muy buen ejercicio.
"""


def max(num1,num2):
    if num1>num2:
        print(f"El número mayor es {num1}")
    elif(num2>num1):
        print(f"El número mayor es {num2}")

