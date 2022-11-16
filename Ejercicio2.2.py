"""Ejercicio 2.2
Definir una función max_de_tres(), que tome tres números como argumentos y
devuelva el mayor de ellos."""

def max_de_tres(num1,num2,num3):
    mayor = 0
        if num1 >= num2:
            mayor = num1
        elif num2 >= mayor:
            mayor = num2
        elif num3 >= mayor:
            mayor = num3
        print(mayor)

max_de_tres(1,3,4)