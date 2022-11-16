"""Ejercicio 1.2
Solicitar al usuario dos valores:
● numero1 (int)
● numero2 (int)
Se debe imprimir el mayor de los dos números (la salida debe ser idéntica a la que
sigue):
Proporciona el numero1:
Proporciona el numero2:
El numero mayor es:<numeroMayor>
¿Cuál es el código del requerimiento solicitado?"""

print("Proporciona el numero1:")
uno = int(input())
print("Proporciona el numero2:")
dos = int(input())


def mayor(num1,num2):
    if num1 > num2:
        print(f"El número mayor es {num1}")
    elif num2 > num1:
        print(f"El número mayor es {num2}")
    else:
        print("Los números introducidos son iguales")

mayor(uno,dos)

