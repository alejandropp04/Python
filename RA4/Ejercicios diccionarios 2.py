#Ejercicios diccionarios 2
'''Ejercicio 1: Escribir un programa que guarde en una  variable el diccionario
 Monedas =  {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por una divisa
 y muestre su simbolo o un mensaje de aviso si la divisa no esta en el dicionario'''

monedas = {
    'Euro' : '€',
    'Dollar' : '$',
    'Yen' : '¥'
}

moneda = input("Introduzca una moneda: ")
if moneda.title() in monedas:
    print(monedas[moneda.title()])
else:
    print("La moneda no se encuentra en el diccionario")


'''Ejercicio 2: Escribir un programa que pregunte al usuario por su nombre, edad, direccion, telefono
y que lo guarde en un diccionario. Despues debe mostrar por pantalla el mensaje "<nombre> tiene <edad>
años, vive en <direccion> y su numero de telefono <telefono>'''

nombre = input("Introduzca el nombre: ")
edad = input("Introduzca su edad: ")
direccion = input("Introduzca la direccion: ")
telefono = input("Introduzca su telefono: ")

datos = {
    "nombre" : nombre,
    "edad" : edad,
    "direccion" : direccion,
    "telefono" : telefono
}

print(f"{datos["nombre"]} tiene {datos["edad"]} años, vive en {datos["direccion"]} y su numero de telefono es {datos["telefono"]}")


'''Ejercicio 3: Escribir un programa que guarde en un diccionario los precios de las frutas de la siguiente tabla:
Fruta      Precio... pregunte al usuario por una fruta, kilos y devuelva el precio de ese numero de kilos de fruta. 
Si la fruta no se encuentra en el diccionario debe mostrar un mensaje informando de ello'''

frutas = {
    'Platanos' : 1.35,
    'Manzanas' : 0.80,
    'Peras' : 0.85,
    'Naranjas' : 0.70
}

fruta = input("Introduzca una fruta: ")
kilos = float(input("Introduzca los kilos: "))

if fruta.title() in frutas:
    precio = frutas[fruta.title()] * kilos
    print(f"El precio de {kilos} kilos de {fruta.title()} es {round(precio, 2)} euros.")
else:
    print("La fruta no se encuentra en el diccionario.")


'''Ejercicio 4: Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y muestre por pantalla el dia, mes (nombre del mes)
y el año en formato dd de <mes> de aaaa'''

fecha = input("Introduzca una fecha en formato dd/mm/aaaa:")
dia, mes, anio = fecha.split("/")
meses = {
    '01' : 'Enero',
    '02' : 'Febrero',
    '03' : 'Marzo',
    '04' : 'Abril',
    '05' : 'Mayo',
    '06' : 'Junio',
    '07' : 'Julio',
    '08' : 'Agosto',
    '09' : 'Septiembre',
    '10' : 'Octubre',
    '11' : 'Noviembre',
    '12' : 'Diciembre'
}

print(f"{dia} de {meses[mes]} de {anio}")

'''Ejercicio 5: Escribir un programa que almacene el diccionario con las notas de las asignaturas de un curso
{'Matematicas': 6, 'Fisica': 7, 'Quimica': 5} y despues muestre por pantalla la nota de cada asignatura
en el formato <asignatura> tiene <nota> puntos. Al final debe de mostrar el numero total de notas del curso'''

notas = {
    'Matematicas' : 6,
    'Fisica' : 7,
    'Quimica' : 5
}
total_notas = 0
for asignatura, nota in notas.items():
    print(f'{asignatura} tiene {nota} puntos.')
    total_notas += nota
print(f'El numero total de notas del curso es: {total_notas}')


'''Ejercicio 6: Escribir un  programa que cree un diccionairo vacio y lo vaya llenando con informacion de una persona
(nombre, edad, sexo, telefono) que se le pida al usuario. Cada vez que se añada un nuevo valor debe imprimirse el contenido del diccionario
'''

persona = {}
continuar = True
while continuar:
    clave = input('¿Que dato desea introducir?')
    valor = input(clave + ': ')
    persona[clave] = valor
    print(persona)
    continuar = int(input("Pulse 1 para continuar o 0 para salir"))
    if continuar == 0:
        continuar = False

'''Ejercicio 7: Escribir un programa que cree un diccionario simulando una cesta de la compra.
El programa debe preguntar el articulo y su precio y añadir el par al diccionario, hasta que el usuario decida terminar.
Después se debe mostrar por pantalla la lista de la compra y el coste total.'''

compra = {}
total = 0
continuar = True
while continuar:
    clave = input('Introduzca el nombre el articulo: ')
    precio = int(input(clave + 'Introduzca el precio : '))
    compra[clave] = precio
    continuar = int(input("Pulse 1 para continuar o 0 para salir: "))
    total += precio
    if continuar == 0:
        continuar = False

for articulo in compra.items():
    print(clave, '\t', precio)
print(f'Total de la compra: {total}')

'''Ejercicio 8: Escribir un programa que cree un diccionario de traduccion español - ingles. El usuario introducirá las palabras en español
 e ingles separadas por dos puntos y cada par <palabra>:<traduccion> separador por comas. El programa debe crear un diccionario con las palabras y sus traducciones.'''

traduccion = {}

frase = input("introduzca una frase en formato <palabra>:<traducciom>, separada por comas: ")

for i in frase.split(","):
    clave, valor = i.split(":")
    traduccion[clave.strip()] = valor.strip()
frase_espanyol = input("Introduzca la frase en español:")
for i in frase_espanyol.split():
    if i in traduccion:
        print(traduccion[i], end=" ")
    else:
        print(i, end=" ")

