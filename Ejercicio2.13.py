"""Ejercicio 2.13
Escribir un programa que le diga al usuario que ingrese una cadena. El programa tiene
que evaluar la cadena y decir cuantas letras mayúsculas tiene."""

cadena = input("Introduce una cadena para contar las mayúsculas: ")

def pide_cadena(cad):
    cont = 0
    if cad.islower() == True:
        cont = 0
    else:
        for i in cad:
            if i.isupper() == True: """Comprueba letra por letra si es mayúscula o no, y suma 1 en el contador si lo es."""
                cont += 1
    return cont

if pide_cadena(cadena) == 0:
    print("La cadena no tiene mayúsculas")
else:
    print(f"La cadena tiene {pide_cadena(cadena)} mayúsculas")





