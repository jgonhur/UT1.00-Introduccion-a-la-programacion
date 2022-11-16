"""Ejercicio 1.1
El objetivo del ejercicio es crear un sistema de calificaciones, como sigue:
El usuario proporcionará un valor entre 0 y 10.
Si está entre 9 y 10: imprimir una A
Si está entre 8 y menor a 9: imprimir una B
Si está entre 7 y menor a 8: imprimir una C
Si está entre 6 y menor a 7: imprimir una D
Si está entre 0 y menor a 6: imprimir una F
cualquier otro valor debe imprimir: Valor desconocido
Por ejemplo:
Proporciona un valor entre 0 y 10:
A
Puedes utilizar el IDE de tu preferencia para codificar la solución y después pegar tu
solución en esta herramienta."""

print("Introduzca una nota entre 0 y 10")
notita = int(input())

def calificacion(notita):
    if (notita >= 0):
        if (notita >= 9) and (notita <= 10):
            calificacion = 'A'
        elif (notita >= 8) and (notita <= 9):
            calificacion = 'B'
        elif (notita >= 7) and (notita <= 8):
            calificacion = 'C'
        elif (notita >= 6) and (notita <= 7):
            calificacion = 'D'
        else:
            calificacion = 'F'
    else:
        print("La nota introducida no es válida")

    print(f"La calificación obtenida es: {calificacion}")

calificacion(notita)