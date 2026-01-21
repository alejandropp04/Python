#Crea un programa que pida numeroa sl usuario hasta que se introduzca un cero

numeros = []
suma = 0
while True:
    num = int(input("Introduzca un numero o 0 para finalizar: "))
    if num == 0:
        break
    numeros.append(num)

print(f"Lista completa de numeros: {numeros}")


print(f"Suma de todos los numeros: {sum(numeros)}")
print(f"Numero mayor: {max(numeros)}")
print(f"Numero menor: {min(numeros)}")
print(f"Media de los numeros: {sum(numeros)/len(numeros)}")

#lista ordenada
numeros.sort()
print(f"Lista ordenada: {numeros}")


# Crea un programa que pida al usuario que introduzca nombres hasta que escriba fin
# Guarda todos los nombres en una lista, muestrea la lista completa
# indica cuantos nombres se han introducido, el mas largo y cuantos empiezan por vocal

nombres = []

while True:
    nombre = input("Introduzca un nombre o 'fin' para finalizar: ")
    if nombre == "fin":
        break
    nombres.append(nombre)

print(f"Lista de nombres: {nombres}")
print(f"Nombres introducidos: {len(nombres)}")

nombre_vocal = 0
longitud_nombre = 0
nombre_largo = ""
for nombre in nombres:
    if nombre.startswith(("a", "e", "i", "o", "u")):
        nombre_vocal += 1
    if len(nombre) > longitud_nombre:
        longitud_nombre = len(nombre)
        nombre_largo = nombre

print(f"Nombres que empiezan por vocales: {nombre_vocal}")
print(f"Nombre mas largo: {nombre_largo}")
nombres.sort()
print(f"Lista ordenada: {nombres}")


''' Crea un programa que permita gerstionar una lista de calificaciones de estudiantes.
    1. Pedir que introduzca calificaciones del 0 - 10
    2. Guardarlas en una lista
    3. Dejar de pedir calificaciones cuando se introduzca el -1
    4. Mostrar la lista completa
    5. Calcular y mostrar nota media, mas baja y mas alta
    6. Mostrar cuantos han aprobado >= 5'''


notas = []
aprobados = 0
while True:
    nota = int(input("Introduzca una nota o -1 para salir"))
    if nota == -1:
        break
    if nota >= 5:
        aprobados += 1
    notas.append(nota)

print(notas)
print(f"La nota mas alta es: {max(notas)}")
print(f"La nota mas baja es: {min(notas)}")
print(f"La media de la lista es: {sum(notas) / len(notas)}")
print(f"Aprobados en la lista: {aprobados}")


''' Crea un programa que añada numeros a una lista.
    Cree dos listas una de pares y otra de impares
    Muestra las 3 listas'''

numeros = []
pares = []
impares = []

while True:
    num = int(input("Introduzca un numero o 0 para finalizar: "))
    if num == 0:
        break
    numeros.append(num)
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

print(f"Lista de numeros: {numeros}")
print(f"Lista de pares: {pares}")
print(f"Lista de impares: {impares}")