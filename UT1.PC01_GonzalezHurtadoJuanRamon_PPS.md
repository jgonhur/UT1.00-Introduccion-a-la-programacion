
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
nombre_funcion($parametro){ 
$variable
return variable;
}
~~~

Cabe mencionar que en C se hace uso de una función principal en los programas llamada
main, esta función retorna 0 si no es de tipo void (no retorna nada). Además C utiliza librerías que deben ser declaradas al principio del programa.


~~~
#include <stdio.h>

int main(){ 
return 0;
}
~~~










