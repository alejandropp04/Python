#Ejercicio de diccionario anidado:
"""
Genera un diccionario para los alumnos de daw2, en el cual haya un diccionario
por cada alumno con su nombre, asignatura (python) y nota, si es menor que 5 
se actualizara la nota a 5
"""

daw2 = {
    "alumno1" : {
        "nombre" : "Ana",
        "asignatura" : "python",
        "nota" : 4
    },
    "alumno2" : {
        "nombre" : "Alejandro",
        "asignatura" : "python",
        "nota" : 8
    },
    "alumno3" : {
        "nombre" : "Luis",
        "asignatura" : "DIW",
        "nota" : 2
    },
    "alumno4" :{
        "nombre" : "Maria",
        "asignatura" : "DWEC",
        "nota" : 6
    }
}

for alumno, datos in daw2.items():
    if datos["asignatura"] == "python" and datos["nota"] < 5:
        datos["nota"] = 5

for alumno, datos in daw2.items():
    print(alumno)
    for clave, valor in datos.items():
        print(f"{clave}:{valor}")