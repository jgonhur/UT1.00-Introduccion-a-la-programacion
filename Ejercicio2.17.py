"""Ejercicio 2.17
Crear una función contar_vocales(), que reciba una palabra y cuente cuantas letras "a"
tiene, cuantas letras "e" tiene y así hasta completar todas las vocales.
Se puede hacer que el usuario sea quien elija la palabra."""

p = 'conserje'
vocales = 'aeiou'
def contar_vocales(palabra):
    a = 0
    e = 0
    i = 0
    o = 0
    u = 0

    for j in palabra:
        if j == 'a':
            a += 1
        elif j == 'e':
            e += 1
        elif j == 'i':
            i += 1
        elif j == 'o':
            o += 1
        elif j == 'u':
            u += 1
    letras = [a, e, i, o, u]

    return letras








