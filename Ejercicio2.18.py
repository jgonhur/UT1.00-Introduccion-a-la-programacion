"""Ejercicio 2.18
Escriba una función es_bisiesto() que determine si un año determinado es un año
bisiesto.Un año bisiesto es divisible por 4, pero no por 100. También es divisible por 400"""

ano = 2400
def es_bisiesto(a):
    sw = 0
    if a % 4 == 0:
        if a % 100 == 0 and a % 400 == 0:
            sw = 1
    return sw

if es_bisiesto(ano) == 1:
    print(f"El año {ano} es bisiesto")
else:
    print(f"El año {ano} no es bisiesto")