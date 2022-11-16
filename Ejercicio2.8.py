"""Ejercicio 2.8
Definir una función generar_n_caracteres() que tome un entero n y devuelva el
caracter multiplicado por n. Por ejemplo: generar_n_caracteres(5, "x") debería devolver
"xxxxx"."""

def generar_n_caracteres(n,letra):
    cadena = ''
    for i in range(n):
        cadena = cadena + letra
    return cadena

print(generar_n_caracteres(5,'pito '))
