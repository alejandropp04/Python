#Ejercicio 1: Contar el numero de filas de un csv
import csv
with open("personas.csv", "r") as f:
    lector = csv.reader(f)
    next(lector)
    filas = sum(1 for fila in lector)
print(f"Numero de filas: {filas}")

#Ejercicio 2: Mostrar solo el nombre de cada persona
with open("personas.csv", "r") as f:
    lector = csv.DictReader(f)
    for linea in lector:
        print(linea["nombre"])

#Ejercicio 3: Calcular el promedio de una columna numerica
total_notas = 0
contador = 0
with open("notas.csv", "r") as f:
    lector = csv.DictReader(f)
    for linea in lector:
        total_notas +=float(linea["nota"])
        contador += 1
promedio = total_notas / contador
print(f"Promedio de notas: {promedio:.2f}")

#Lista de frutas para añadir
lista_frutas = [
    ["Cherry", "0.75", "20"],
    ["Peras", "2.25", "120"]
]
#Ejercicio 4: Escribir datos en un archivo csv
with open("stock.csv", "a") as f:
    escritor = csv.writer(f)
    #Añadir lista a lista
    escritor.writerow(["PLatanos", "2,25", "50"])
    escritor.writerow(["sandias", "0,75", "30"])
    #Si quiero añadir mas listas, le paso una lista
    escritor.writerows(lista_frutas)

#Lista de diccionarios para añadir
lista_diccionario = [
    {"nombre": "Alejandro", "apellido": "Pacheco"},
    {"nombre": "Carlos", "apellido": "Aguilar"}
]

#Ejercicio 5: Escribir en un archivo con un diccionario
with open("datos.csv", "a") as f:
    escritor = csv.DictWriter(f, fieldnames=["nombre", "apellido"])
    escritor.writeheader()  # Escribir la cabecera
    escritor.writerows(lista_diccionario) #Añadiendo uns lista de diccionarios
    escritor.writerow({"nombre": "Lucia", "apellido": "Gomez"}) #Añadiendo un diccionario individualmente

#Ejercicio 7: Añadir filas a un archivo csv.
lista_inventario = [
    {"producto": "Grapadora", "precio": "12.99", "cantidad": "15"},
    {"producto": "Boligrafo", "precio": "0.99", "cantidad": "500"},
    {"producto": "Cuaderno", "precio": "3.49", "cantidad": "5"}
]
with open("inventario.csv", "a") as f:
    escritor = csv.DictWriter(f, fieldnames=["producto", "precio", "cantidad"])
    escritor.writeheader()  # Escribir la cabecera
    #Si la cantidad es mayor a 10, se añade al archivo
    for item in lista_inventario:
        if int(item["cantidad"]) > 10:
            escritor.writerow(item)

with open("inventario.csv") as f:
    for linea in f:
        print(linea)

#Ejercicio 8: Escribir multiples filas usando DictWriter
estudiantes = [
    {"nombre": "Juan", "edad": "20", "grado": "A"},
    {"nombre": "Ana", "edad": "22", "grado": "B"},
    {"nombre": "Luis", "edad": "21", "grado": "A"},
    {"nombre": "Ana", "edad": "23", "grado": "C"}
]

with open("estudiantes.csv", "w") as f:
    escritor = csv.DictWriter(f, fieldnames=["nombre", "edad", "grado"])
    escritor.writeheader()  # Escribir la cabecera
    escritor.writerows(estudiantes)  # Escribir múltiples filas a la vez

with open("estudiantes.csv") as f:
    for linea in f:
        print(linea)

#Ejercicio 9: Buscar un registro específico en un archivo CSV
nombre = input("Ingrese el nombre del estudiante a buscar: ")

with open("estudiantes.csv", "r") as f:
    lector = csv.DictReader(f)
    for linea in lector:
        if linea["nombre"].lower() == nombre.lower():
            print(f"Detalles del estudiante: {linea}")
        with open("estudiante_encontrado.csv", "a") as f_encontrado:
                escritor = csv.DictWriter(f_encontrado, fieldnames=lector.fieldnames)
                escritor.writeheader()
                escritor.writerow(linea)