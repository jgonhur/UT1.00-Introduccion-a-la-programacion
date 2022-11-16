"""Ejercicio 2.9
Definir un histograma procedimiento() que tome una lista de números enteros e
imprima un histograma en la pantalla. Ejemplo: procedimiento([4, 9, 7]) debería imprimir
lo siguiente:"""

lista = [2,4,6,7,1,4,5,8,1,8,3,17,8]

def procedimiento(l):
    for i in l:
        for j in range(i):
            print(f"{i} ",end = "")
        print()
procedimiento(lista)