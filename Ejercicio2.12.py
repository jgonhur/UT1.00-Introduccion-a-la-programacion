"""Ejercicio 2.12
Escribir una función filtrar_palabras() que tome una lista de palabras y un entero n, y
devuelva las palabras que tengan más de n caracteres."""

listap=['marco','polo','do','it','faster','stronger','onomastica']
n = 6
def filtrar_palabras(lp,n):
    pgrande = []
    for i in lp:
        if longitud(i) > n:
            pgrande.append(i)
    return pgrande
def longitud(c):
    cont = 0
    for i in c:
        cont += 1
    return cont

print(filtrar_palabras(listap,n))