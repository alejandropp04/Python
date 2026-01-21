# Crea un programa que solicite una cadena uy cuente cuantas palabras tiene
cadena = input("Introduzca un frase: ").lower().replace(", ", " ").replace("."," ").replace(";", " ").replace(":", " ")

palabras = cadena.split()

diccionario_palabras = {}

for palabra in palabras:
    if palabra in diccionario_palabras:
        diccionario_palabras[palabra] += 1
    else:
        diccionario_palabras[palabra] = 1
print(f"El numero total de palabras es: {len(palabras)}")
for palabra, cantidad in diccionario_palabras.items():
    print(f"La palabra '{palabra}' se repite {cantidad} veces")