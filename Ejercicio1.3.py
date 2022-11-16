"""Ejercicio 1.3
Iterar un rango de 0 a 10 e imprimir sólo los números divisibles entre 3"""


def tresdiv():
    a = 0
    while (a <= 10):
        if (a % 3 == 0):
            print(f"{a} ",end="")
        a += 1

tresdiv()