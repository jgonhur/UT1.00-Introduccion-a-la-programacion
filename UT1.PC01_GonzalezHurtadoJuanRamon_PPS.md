
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
- Uso del bucle **while**.
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
    else:
        print(f"{num1} y {num2} son iguales")
~~~
- Uso de funciones, estructuras condicionales.
- La función hace uso de dos parámetros para su comparación.
~~~
"""Ejercicio 2.2
Definir una función max_de_tres(), que tome tres números como argumentos y
devuelva el mayor de ellos."""

def max_de_tres(num1,num2,num3):
    mayor = 0
        if num1 >= num2:
            mayor = num1
        elif num2 >= mayor:
            mayor = num2
        elif num3 >= mayor:
            mayor = num3
        print(mayor)

max_de_tres(1,3,4)
~~~
- Uso de funciones, estructuras condicionales.
- Se introducen en la función tres parámetros.
~~~
"""Ejercicio 2.3
Definir una función que calcule la longitud de una lista o una cadena dada. (Es cierto
que python tiene la función len() incorporada, pero escribirla por nosotros mismos
resulta un muy buen ejercicio."""


def longitud(cadena):
    a = 0
    if type(cadena) == str:
        for i in cadena:
                a += 1
        return a
    else:
        print("Cadena no válida")
~~~
- Uso del **contador** a, para determinar el número de letras en la palabra introducida
como parámetro. Este número de letras determinaría la longitud de la cadena.
- Uso de control de errores, comprobando si la cadena es una variable de tipo string o no.
- Uso de bucle for para recorrer los elementos de la cadena
~~~
"""Ejercicio 2.4
Escribir una función que tome un carácter y devuelva True si es una vocal, de lo
contrario devuelve False."""


def vocal(caracter):
    vocales= ['a','e','i','o','u','A','E','I','O','U']
    if caracter in vocales:
        print("True")
    else:
        print("False")

vocal('I')
~~~
- Se declara una lista con las vocales en minúsculas y mayúsculas, para comprobar
si coincide el elemento de la cadena con un elemento de la lista.
~~~
"""Ejercicio 2.5
Escribir una función sum() y una función multip() que sumen y multipliquen
respectivamente todos los números de una lista. Por ejemplo: sum([1,2,3,4]) debería
devolver 10 y multip([1,2,3,4]) debería devolver 24."""

lista=[1,2,3,9]

def sum(lista):
    total = 0
    for i in lista:
        total = total + i
    print(total)


def multip(lista):
    total = 1
    for i in lista:
        total = total * i
    print(total)

sum(lista)
multip(lista)
~~~
- Uso de funciones, bucles for y llamadas a las funciones, usando la lista de números
como parámetro para ambas.
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

print(inverso(cadena))
~~~
- Declaración de una cadena de caracteres vacía.
- Uso de función longitud (sustituyendo len).
- El bucle for lee la cadena desde el final al principio, introduciéndola en la variable
anedac.

~~~
"""Ejercicio 2.7
Definir una función superposicion() que tome dos listas y devuelva True si tienen al
menos 1 miembro en común o devuelva False de lo contrario. Escribir la función usando
el bucle for anidado."""

lista1 = [11,4,2,3235,21,3,5,27]
lista2= [1,78,45,34,23]

def superposicion(l1,l2):
    sw = 'False'
    for i in l1:
        for j in l2:
            if j == i:
                sw = 'True'
    return sw

print(superposicion(lista1,lista2))
~~~
- Uso de switch para marcar el cumplimiento de una condición. Este indica cuándo se cumple
la condición de que un elemento de una lista, sea igual a un elemento de la otra.
~~~
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

~~~
- Uso de cadenas de caracteres y bucle for para recorrerla.
~~~
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
~~~
- Lista los números en filas, de manera que crea un histograma.
- El bucle for hace una lista con el mismo número.
- También se puede repetir el elemento de la cadena usando *=
~~~
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
~~~
- Declaramos una acumulador, inicializado con el primer valor, para que al final guarde
el valor máximo.
- Uso de estructurasde control.
~~~
"""Ejercicio 2.11
Escribir una función mas_larga() que tome una lista de palabras y devuelva la más larga."""

lista = ['patata','pionono de patas verdes blanco','pato','alambrada','barba','ornitorrinco','anacardo','bandera','pionono de patas verdes']

def mas_larga(p):
    plarga = p[0]
    for i in p:
        if longitud(i) > longitud(plarga):
            plarga = i
    return plarga

def longitud(c):
    cont = 0
    for i in c:
        cont += 1
    return cont


print(mas_larga(lista))
~~~
- Uso de bucles for, contadores, estructuras de control y cadena de caracteres.
- Calcula la longitud de las palabras y las guarda en una lista "plarga".

~~~
"""Ejercicio 2.12
Escribir una función filtrar_palabras() que tome una lista de palabras y un entero n, y
devuelva las palabras que tengan más de n caracteres."""

listap=['marco','polo','do','it','faster','stronger','onomastica']
n = 6
def filtrar_palabras(lp,n):
    pgrande = []
    for i in lp:
        if longitud(i) > n:
            pgrande.append(i)
    return pgrande
def longitud(c):
    cont = 0
    for i in c:
        cont += 1
    return cont

print(filtrar_palabras(listap,n))
~~~
- Usa la función append, que añade los elementos a la lista que precede al punto
~~~
~~~

~~~
~~~

~~~
~~~

~~~
~~~










