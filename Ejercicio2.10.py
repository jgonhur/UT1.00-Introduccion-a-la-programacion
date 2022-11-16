"""Ejercicio 2.10
La función max() del ejercicio 1 (primera parte) y la función max_de_tres() del ejercicio
2 (primera parte), solo van a funcionar para 2 o 3 números. Supongamos que tenemos
más de 3 números o no sabemos cuántos números son. Escribir una función
max_in_list() que tome una lista de números y devuelva el más grande."""

lista = [1,654,54,54,65,132,1323,3,50,1,61,6,41,3,-62035]

def max_in_list(lista):
    max = lista[0]
    for i in lista:
        if i > max:
            max = i
    return max

print(max_in_list(lista))

