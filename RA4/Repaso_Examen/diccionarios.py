'''Tienes una lista de estudiantes con sus notas. Crea un diccionario donde la clave sea el estudiante y la nota el valor
    1. Imprime todas las notas
    2. Imprime el estudiante con la nota mas alta
    3. Permite buscar la nota de un estudiante introduciendo su nombre'''

estudiantes ={
    "Ana" : 8,
    "Luis"  : 7,
    "Marta" : 9,
    "Jorge" : 6
}

for clave, valor in estudiantes.items():
    print(f"{clave} : {valor}")

mejor_estudiante = max(estudiantes, key=estudiantes.get)
print(f"El estudiante con mayor nota es: {mejor_estudiante}")

buscar = input("Introduzca el nombre del estudiante que desea buscar: ")

if buscar in estudiantes:
    print(f"El estudiante {buscar} tiene la nota : {estudiantes[buscar]}")
else:
    print(f"El estudiante {buscar} no se encuentra en la lista")



''' A traves de esta string pasalo a diccionario
"usuario1:contraseña1,usuario2:contraseña2,usuario3:contraseña3"'''

cadena = "usuario1:contraseña1,usuario2:contraseña2,usuario3:contraseña3"

usuarios = {}

for palabra in cadena.split(","):
    clave, valor = palabra.split(":")
    usuarios[clave] = valor

for usuario in usuarios.items():
    print(usuario)