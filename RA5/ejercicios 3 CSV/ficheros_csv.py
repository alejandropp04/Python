import csv
#Leer el fichero CSV y mostrar su contenido
with open("personas.csv", "r") as f:
    for linea in f:
        print(linea.strip())

#2. Leer CSV con el modulo csv integrado en python
print("\n Leer CSV con modulo integrado con Python")
with open("personas.csv", "r") as f:
    lector = csv.reader(f) #delimiter="," por defecto es la coma
    next(lector)  # Saltar la primera línea (cabecera)
    for linea in lector:
        print(linea)

#3. Leer CSV como diccionario
print("\n Leer CSV como diccionario")
with open("personas.csv", "r") as f:
    lector = csv.DictReader(f)
    next(lector)  # Saltar la primera línea (cabecera)
    for linea in lector:
        print(linea)

#4. Leer el csv como diccionario delimitado por ;
print("\n Leer CSV como diccionario delimitado por ;")
with open("personas2.csv", "r") as f:
    lector = csv.DictReader(f, delimiter=";")
    next(lector)  # Saltar la primera línea (cabecera)
    for linea in lector:
        print(linea)
    f.seek(0)  # Volver al inicio del archivo para leerlo de nuevo
    
    for linea in lector:
        print(f"Nombre: {linea['nombre']}, DNI: {linea['dni']}")


#5. Leer el csv como diccionario mostrando el nombre y el DNI
print("\n Leer CSV como diccionario mostrando el nombre y el DNI")
with open("personas.csv", "r") as f:
    lector = csv.DictReader(f)
    next(lector)
    for linea in lector:
        print(f"Nombre: {linea['nombre']}, DNI: {linea['dni']}")