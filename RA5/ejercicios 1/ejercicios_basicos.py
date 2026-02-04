#EJ1: Mostrar el contenido del ficheor por consola
with open("datos.txt", "r") as f:
    print(f.read())

#EJ2: Programa que cuente cuantas lineas tiene el archivo
with open("datos.txt", "r") as f:
    lineas = f.readlines() #Guarda en una lista las lineas, 1 por 1
    print(f"Numero de lineas: {len(lineas)}")

#EJ3: Buscar una palabra en un fichero
palabra = input("Introduzca una palabra a buscar en el fichero: ")
with open("datos.txt", "r") as f:
    contenido = f.read()
    total = contenido.count(palabra)
    print(f"La palabra {palabra}, aparece {total} veces")

#EJ4: Escribir en un fichero
with open("nuevo.txt", "w") as f:
    while True:
        linea = input("Introduzca una linea (o 'salir' para terminar): ")
        if linea.lower() == 'salir':
            break
        f.write(linea + "\n")
    f.close()

#EJ5: Añadir texto a un fichero existente
with open("datos.txt", "a") as f:
    while True:
        linea = input("Introduzca una linea para añadir (o 'salir' para terminar): ")
        if linea.lower() == 'salir':
            break
        f.write(linea + "\n")
    f.close()
    
#EJ6: Copiar el contenido de un fichero a otro
with open("datos.txt", "r") as origen:
    with open("copia_datos.txt", "w") as destino:
        for linea in origen:
            destino.write(linea)
    destino.close()
    origen.close()

#EJ7: Invertir el contenido de un fichero
with open("datos.txt", "r") as f:
    lineas = f.readlines()
with open("invertido.txt", "w") as f:
    for linea in reversed(lineas):
        f.write(linea)
    f.close()