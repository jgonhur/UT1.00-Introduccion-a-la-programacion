"""Ejercicio 2.14
Construir un pequeño programa que convierta números binarios en enteros.
Ejercicio 6
Escribir un pequeño programa donde:
- Se ingresa el año en curso.
- Se ingresa el nombre y el año de nacimiento de tres personas.
- Se calcula cuántos años cumplirán durante el año en curso.
- Se imprime en pantalla."""

binario = 1010101
bin = str(binario)

def bin_dec(b):
    d = 0
    for i in range(longitud(b)):
        if b[i-1] == 1:
            d = d + 2**(i-1)
    return d



def longitud(c):
    cont = 0
    for i in c:
        cont += 1
    return cont

print(bin_dec(bin))