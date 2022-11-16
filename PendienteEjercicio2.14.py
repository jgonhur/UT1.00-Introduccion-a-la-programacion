"""Ejercicio 2.14
Construir un pequeño programa que convierta números binarios en enteros.
Ejercicio 6
Escribir un pequeño programa donde:
- Se ingresa el año en curso.
- Se ingresa el nombre y el año de nacimiento de tres personas.
- Se calcula cuántos años cumplirán durante el año en curso.
- Se imprime en pantalla."""

binario = input("Introduzca un número binario: ")
bin = str(binario)

def bin_dec(b):
    d = 0
    for i in range(len(b)-1):

            d = d + int(b[i])*(2**i)
            print(f"{d}\n")
    return d

bin_dec(bin)



def longitud(c):
    cont = 0
    for i in c:
        cont += 1
    return cont

print(bin_dec(bin))