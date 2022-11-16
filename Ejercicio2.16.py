"""Ejercicio 2.16
Definir una lista con un conjunto de nombres, imprimir la cantidad de comienzan con la
letra a.
También se puede hacer elegir al usuario la letra a buscar. (Un poco mas emocionante)"""

listan= ['ana','pepe','paco','cristina','perico','geronimo','andres','agustin']

def funcion_a(lista):
    anombre=[]
    for i in lista:
        for j in lista[i]:
            if lista[i] == 'a':
                anombre.append(i)
    return anombre

funcion_a(listan)

