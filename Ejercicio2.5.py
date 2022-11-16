"""Ejercicio 2.5
Escribir una función sum() y una función multip() que sumen y multipliquen
respectivamente todos los números de una lista. Por ejemplo: sum([1,2,3,4]) debería
devolver 10 y multip([1,2,3,4]) debería devolver 24."""

lista=[1,2,3,9]

def sum(lista):
    total = 0
    for i in lista:
        total = total + i
    print(total)


def multip(lista):
    total = 1
    for i in lista:
        total = total * i
    print(total)

sum(lista)
multip(lista)