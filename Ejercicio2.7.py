"""Ejercicio 2.7
Definir una función superposicion() que tome dos listas y devuelva True si tienen al
menos 1 miembro en común o devuelva False de lo contrario. Escribir la función usando
el bucle for anidado."""

lista1 = [11,4,2,3235,21,3,5,27]
lista2= [1,78,45,34,23]

def superposicion(l1,l2):
    sw = 'False'
    for i in l1:
        for j in l2:
            if j == i:
                sw = 'True'
    return sw

print(superposicion(lista1,lista2))
