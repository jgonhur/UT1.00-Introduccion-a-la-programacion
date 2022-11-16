"""Ejercicio 2.15
Definir una tupla con 10 edades de personas.
Imprimir la cantidad de personas con edades superiores a 20.
Puedes variar el ejercicio para que sea el usuario quien ingrese las edades."""

print("Introduzca 10 edades diferentes")

def edad_superior():
    listae = []
    for i in range(9):
        a = input()
        if int(a) > 20:
            listae.append(a)
    print(listae)

edad_superior()
