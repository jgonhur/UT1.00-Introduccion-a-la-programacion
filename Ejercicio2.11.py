"""Ejercicio 2.11
Escribir una función mas_larga() que tome una lista de palabras y devuelva la más larga."""

lista = ['patata','pionono de patas verdes blanco','pato','alambrada','barba','ornitorrinco','anacardo','bandera','pionono de patas verdes']

def mas_larga(p):
    plarga = p[0]
    for i in p:
        if longitud(i) > longitud(plarga):
            plarga = i
    return plarga

def longitud(c):
    cont = 0
    for i in c:
        cont += 1
    return cont


print(mas_larga(lista))
