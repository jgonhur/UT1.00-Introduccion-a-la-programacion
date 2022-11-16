"""Ejercicio 2.17
Crear una función contar_vocales(), que reciba una palabra y cuente cuantas letras "a"
tiene, cuantas letras "e" tiene y así hasta completar todas las vocales.
Se puede hacer que el usuario sea quien elija la palabra."""

p = 'conserje'

def contar_vocales(palabra):
    lista = {'a' : 0, 'e' : 0, 'i' : 0, 'o' : 0,'u' : 0}
    for letra in palabra:
        for vocal in lista:
            if vocal == letra:
                lista[vocal] += 1
    return voca

print(contar_vocales(p))







