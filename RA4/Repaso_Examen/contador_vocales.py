#Crea un programa que solicite al usuario una cadena y diga cuantas vocales tiene
# 1. Recibir una cadena de texto
# 2. Contar cuantas vocales tiene, sin distinguir entre mayusculas y minusculas
# 3. Mostrar el numero total de vocales
# 4. Mostrar el conteo individual de cada vocal

cadena = input("Introduzca una cadena: ")

cadena = cadena.lower()

vocales = {
    "a" : 0,
    "e" : 0,
    "i" : 0,
    "o" : 0,
    "u" : 0
}

total_vocales = 0

for letra in cadena: 
    if letra in vocales:
        vocales[letra] += 1
        total_vocales += 1

print(f"Total de vocales: {total_vocales}")

for vocal, cantidad in vocales.items():
    print(f"{vocal} : {cantidad}")