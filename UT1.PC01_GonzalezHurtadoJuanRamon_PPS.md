
# UT1 - Prueba calificable 01 Fundamentos de la programación

### Puesta en Producción Segura

## Introducción

En este trabajo vamos a tratar las principales características de la 
programación en Python y vamos a diferenciarlas del otros lenguajes de
programación.

Para empezar comenzaremos con una enumeración de las **principales características
de Python**:

- Es un lenguaje **interpretado**.
- Tiene un **tipado dinámico**.
- Es **fuertemente tipado**.
- Es un lenguaje **multiplataforma**.
- Es **orientado a objetos**.

También podemos decir que usa la indentación para definir dónde comienza y acaba un
bloque de código. Por ejemplo:

~~~
def mayor(a,b):
    mayor = a
    if b > a:
        print("b es mayor")
    elif a == b:
        print("a y b son iguales")
    else:
        print("a es mayor")
~~~

## Comparación de Python con otros lenguajes de programación


He seleccionado los ejercicios 1.3, 2.6 y 2.13 de la relación de ejercicios provistos
en la práctica UT1.00.

Haremos una comparativa de Python con otros lenguajes de 
programación. Estos lenguajes serán PHP y C.

~~~
"""Ejercicio 1.3
Iterar un rango de 0 a 10 e imprimir sólo los números divisibles entre 3"""


def tresdiv():
    a = 0
    while (a <= 10):
        if (a % 3 == 0):
            print(f"{a} ",end="")
        a += 1
~~~
~~~
"""Ejercicio 2.6
Definir una función inversa() que calcule la inversión de una cadena. Por ejemplo la
cadena "estoy probando" debería devolver la cadena "odnaborp yotse"""

cadena='estoy probando'

def inverso(patata):
    anedac = ''
    l=longitud(patata)
    for i in range(l):
        anedac = anedac + patata[l-1-i]
    return anedac

def longitud(cadena):
    a = 0
    if type(cadena) == str:
        for i in cadena:
                a += 1
    else:
        print("Cadena no válida")
    return a
~~~
~~~
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
            if i.isupper() == True:
                cont += 1
    return cont

if pide_cadena(cadena) == 0:
    print("La cadena no tiene mayúsculas")
else:
    print(f"La cadena tiene {pide_cadena(cadena)} mayúsculas")
~~~

Podemos observar que Python no utiliza llaves para diferenciar los bloques de programación
como podemos ver en las estructuras condicionales y en la definición de funciones.

Sin embargo en PHP y en C tenemos que diferenciar los bloques con llaves. Aunque las funciones y
variables en C, al ser un lenguaje fuertemente tipado, tenemos que declararlas junto al tipo de variable
que va a devolver, como sigue.

~~~
int nombre_funcion(parametros){ 
int n_entero;
return n_entero;
}
~~~

En cambio en PHP definiríamos la función y las variables sin indicar el tipo de variable:

~~~
nombre_funcion ($parametro){ 
$variable
return variable;
}
~~~

También podemos decir que la definición de arrays en C y en PHP cambia, esto es:

En PHP:
~~~
$array = {3,45,1}
~~~
En C:
~~~
A[dimension_del_array] = {1,5,2,6} 
~~~
~~~
En Python:
a = [1,23,6,343]
~~~

## Comparación: Python vs C

Cabe mencionar que en C se hace uso de una función principal en los programas llamada
main, esta función retorna 0 si no es de tipo void (no retorna nada). Además C utiliza librerías que deben ser declaradas al principio del programa.


~~~
#include <stdio.h>

int main(){ 
return 0;
}
~~~

Aunque tenemos que hacer varias diferenciaciones entre Python y C. Puesto que Python es un 
lenguaje interpretado y C es compilado. Por otro lado, Python es un lenguaje multiplataforma,
sin embargo, C no es portable.

Otra diferencia que mencionamos anteriormente, es el uso de la función main() de C. A la hora de
la ejecución, en C se ejecuta primero esta función y luego el resto de funciones y llamadas. 

Podría decirse que Python es un lenguaje más práctico para el aprendizaje automático y C lo es 
para aplicaciones empresariales o integradas. 

## Uso del código fuente en los ejercicios trabajos
~~~
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
~~~

- En este ejercicio se hace uso de las estructuras condicionales **if, elif y else**
- Uso de una **función** y su correspondiente **llamada**.
- También dentro de las condiciones usamos el operador lógico **and**.
- Mediante **input()** se interactúa con el usuario pidiéndole un dato.
~~~
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
~~~
- Como en el anterior ejercicio se hace uso de funciones y estructuras condicionales.
- **Declaración de variables** que recogen los datos introducidos por el usuario.

~~~
"""Ejercicio 1.3
Iterar un rango de 0 a 10 e imprimir sólo los números divisibles entre 3"""


def tresdiv():
    a = 0
    while (a <= 10):
        if (a % 3 == 0):
            print(f"{a} ",end="")
        a += 1

tresdiv()
~~~
- Uso de la estructura conficional **while**.
- En la función print **end=""** sirve para que Python **no salte por defecto a la siguiente línea**.
- Uso de un **contador** dentro del bucle while que controlará la duración del bucle.
~~~
"""Ejercicio 2.1
Definir una función max() que tome como argumento dos números y devuelva el mayor
de ellos. (Es cierto que python tiene una función max() incorporada, pero hacerla
nosotros mismos es un muy buen ejercicio.
"""


def max(num1,num2):
    if num1>num2:
        print(f"El número mayor es {num1}")
    elif(num2>num1):
        print(f"El número mayor es {num2}")
~~~
- Uso de funciones, estructuras condicionales.
- La función hace uso de dos parámetros para su comparación
~~~
~~~

~~~
~~~

~~~
~~~

~~~
~~~

~~~
~~~









