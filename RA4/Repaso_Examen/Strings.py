# Crea un programa que solicite al usuario una cadena de texto y realice las siguientes operaciones:
# 1. Muestre la cadena original
# 2. Indique cuántos caracteres tiene el texto (sin contar espacios)
# 3. Muestre el texto en mayusculas y minusculas
# 4. Indique si el texto empieza por una vocal
# 5. Reemplace todos los espacios por guiones
# 6. Muestre la primera y la ultima palabra del texto

string = input("Introduzca una frase: ")
print(string)

cont = 0
for caracter in string:
    if(caracter != " "):
        cont += 1

print(f"Caracteres totales sin espacios {cont}")

print(f"Texto en mayusculas: {string.upper()}")
print(f"Texto en minusculas: {string.lower()}")

string_limpia = string.strip().lower()

if string_limpia.startswith(("a", "e", "i", "o", "u")):
    print("La cadena empieza por vocal")
else:
    print("La cadena no empieza por vocal")

string_reemplazada = string.replace(" ", "-")
print(F"Cadena cambiada espacios por guiones: {string_reemplazada}")

palabras = string.split()

print(f"Primera palabra: {palabras[0]}")
print(f"Ultima palabra: {palabras[-1]}")

''' Crea un programa en Python que solicite al usuario una cadena de texto y realice las siguientes operaciones:
    1. Muestre la cadena original
    2. Muestre el numero total de caracteres del texto
    3. Indique cuantas vocales tiene la cadena
    4. muestre el texto invertido
    5. Indique si la cadena es palindromo, se lee igual al reves'''

cadena = input("Introduzca una cadena: ")

print(cadena)

print(f"Numero total de caracteres en la cadena: {len(cadena)}")

vocales = "aeiou"
cont_vocales = 0
for letra in cadena.lower():
    if letra in vocales:
        cont_vocales += 1

print(f"Vocales en la cadena: {cont_vocales}")

cadena_invertida = cadena[::-1]

print(f"Cadena del reves: {cadena_invertida}")

if cadena.lower() == cadena_invertida:
    print("La cadena es palindromo")
else:
    print("La cadena no es palindromo")


'''Crea un progrma que verifique si la contraseña cumple los siguientes requisitos:
1. Debe tener al menos 8 caracteres
2. Debe contener al menos una letra en mayuscula y una en minuscula
3. Debe contener al menos un numero
4. No debe contener espacios'''

contraseña = input("Introduzca una contraseña: ")

errores = []
mayuscula = False
minuscula = False
numero = False

if len(contraseña) < 8:
    errores.append("Debe tener al menos 8 caracteres")

if " " in contraseña:
    errores.append("No debe contener espacios")

for caracter in contraseña:
    if caracter.isdigit():
        numero = True
    if caracter.isupper():
        mayuscula = True
    if caracter.islower():
        minuscula = True

if not numero:
    errores.append("Debe tener un numero")    
if not mayuscula:
    errores.append("Debe tener una mayuscula")
if not minuscula:
    errores.append("Debe tener una miniscula")

if not errores:
    print("Contraseña valida")
else:
    for e in errores:
        print(f" - {e}")