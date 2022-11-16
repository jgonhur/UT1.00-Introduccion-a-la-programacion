"""Ejercicio 2.6
Definir una función inversa() que calcule la inversión de una cadena. Por ejemplo la
cadena "estoy probando" debería devolver la cadena "odnaborp yotse"""

cadena='estoy probando'

def inverso(patata):
    anedac = ''
    l=longitud(patata)
    for i in range(l):
        anedac = anedac + patata[l-1-i]
    return anedac

def longitud(cadena):
    a = 0
    if type(cadena) == str:
        for i in cadena:
                a += 1
    else:
        print("Cadena no válida")
    return a

print(inverso(cadena))

