#Ejercicio 1: Crea una funcion calcular_estadisticas(numeros) que reciba
# una lista de numeros y devuelva una tupla con: max, min y media


def calcular_estadisticas (numeros):
    maximo = max(numeros)
    minimo = min(numeros)
    media = sum(numeros) / len(numeros)
    return maximo, minimo, round(media, 2)


numeros = (11, 35, 20, 65, 54, 12, 1)
print(calcular_estadisticas(numeros))


# Ejercicio 2: Crear una funcion distancia(p1, p2) que reciba dos tuplas 
# representando puntos en el plano (x, y) y devuelva la distancia entre ellos
# usando la formula 

import math
def distancia(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return math.sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))

print (f"Distancia = {distancia((2, 3), (5, 7))}")

#Ejercicio 3: Crea una funcion analizar_texto(texto) que devuelva una tupla
# con: Total de caracteres, numero de palabras, primera palabra del texto

def analizar_texto(texto):
    total = len(texto)
    primer_elemento = texto[0]
    caracteres = 0
    for palabra in texto:
        caracteres += len(palabra)
    return total, caracteres, primer_elemento

texto = ("hola", "buenas", "tardes")
print(analizar_texto(texto))

#Ejercicio 4: Crea una funcion convertir_temperatura(celsius) que reciba celsius
# y devuelva una tupla con la temperatura en Fahrenheit y Kelvin

def convertir_temperatura(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    kelvin = celsius + 273.15
    return fahrenheit, kelvin

print(convertir_temperatura(25))

#Ejercicio 5: Crear una funcion analizar_numeros(numeros) que reciba una lista
# de enteros y devuelva una tupla con el numero de pares, impares y el total

def analizar_numeros(numeross):
    pares = 0
    impares = 0
    total = 0
    for i in numeross:
        if i % 2 == 0:
            pares += numeross.count(i)
        else:
            impares += numeross.count(i)
        total += i
    return pares, impares, total

numeross = (1, 5, 3, 4, 2, 29, 10, 35)
print(analizar_numeros(numeross))

#Ejercicio 6: Crea una funcion procesar_cadena(cadena) que devuelva una tupla
# con: La cadena en mayusculas, en minusculas y la longitud de la cadena
def procesar_cadena(cadena):
    mayusculas = cadena.upper()
    minusculas = cadena.lower()
    longitud = len(cadena)
    return mayusculas, minusculas, longitud

print(procesar_cadena("programacion en python"))