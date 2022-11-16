"""Ejercicio 2.4
Escribir una función que tome un carácter y devuelva True si es una vocal, de lo
contrario devuelve False."""


def vocal(caracter):
    vocales= ['a','e','i','o','u','A','E','I','O','U']
    if caracter in vocales:
        print("True")
    else:
        print("False")

vocal('I')
