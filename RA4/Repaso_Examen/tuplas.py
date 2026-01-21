''' Crea un programa que trabaje con temperaturas en grados Celsius
    1. Definir una tupla con varias temperaturas
    2. Mostrar la tupla completa
    3. Maximo, minimo y media
    4. Crea una nueva tupla ordenada de menor a mayor
    5. Mostrar la tupla ordenada '''

temperaturas = (25, 22, 30, 45, 0, -4, 15)

print(temperaturas)
print(f"Temperatura maxima: {max(temperaturas)}")
print(f"Temperatura minuma: {min(temperaturas)}")
print(f"Media de temperaturas: {sum(temperaturas) / len(temperaturas)}")

ordenadas = sorted(temperaturas)

ordenadasM = sorted(temperaturas, reverse=True)

temp_maxmin = ordenadasM
temp_ordenadas = (ordenadas)

print(f"Temperaturas ordenadas: {temp_ordenadas}")
print(f"Tempereturas ordenadas de max a min: {temp_maxmin}")


''' Adivina en que posicion esta el nº n (aleatorio entre 0 - 10) en una tupla'''
import random
numeros = (1, 5, 6, 2, 10, 9, 8, 7, 3)

n = random.randint(0, 10)

posicion = numeros.index(n)

print(f"El numero aleatorio {n} se encuentra en la posicion {posicion}")
print(numeros)