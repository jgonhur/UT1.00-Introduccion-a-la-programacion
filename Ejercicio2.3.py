"""Ejercicio 2.3
Definir una función que calcule la longitud de una lista o una cadena dada. (Es cierto
que python tiene la función len() incorporada, pero escribirla por nosotros mismos
resulta un muy buen ejercicio."""


def longitud(cadena):
    a = 0
    if type(cadena) == str:
        for i in cadena:
                a += 1
        return a
    else:
        print("Cadena no válida")

longitud(12)