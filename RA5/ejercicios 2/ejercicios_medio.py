#EJ1: contar palabras en un fichero
with open("datos.txt", "r") as f:
    contenido = f.read()
    palabras = contenido.split() #Separa el texto en palabras, usando espacios como separadores
    print(f"Numero de palabras: {len(palabras)}")

#EJ2: Contar la frecuencia de cada palabra en un fichero
with open("datos.txt", "r") as f:
    contenido = f.read()
    palabras = contenido.split()
    frecuencia = {}
    for palabra in palabras:
        palabra = palabra.lower().strip(",.")  # Normalizar la palabra
        if palabra in frecuencia:
            frecuencia[palabra] += 1
        else:
            frecuencia[palabra] = 1
    for palabra, cuenta in frecuencia.items():
        print(f"La palabra '{palabra}' aparece {cuenta} veces.")

#EJ3: filtrar lineas segun palabra clave, muestre solo las lineas que contienen esa palabra
palabra_clave = input("Introduzca la palabra clave para filtrar lineas: ")
with open("datos.txt", "r") as f:
    for linea in f:
        if palabra_clave in linea:
            print(linea.strip())

#EJ4: Reemplazar una palabra en el fichero
palabra_a_reemplazar = input("Introduzca la palabra a reemplazar: ")
nueva_palabra = input("Introduzca la nueva palabra: ")
with open("datos.txt", "r") as f:
    contenido = f.read()
contenido_modificado = contenido.replace(palabra_a_reemplazar, nueva_palabra)
with open("datosr.txt", "w") as f:
    f.write(contenido_modificado)