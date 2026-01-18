#Ejercicios diccionarios 1

'''Ejercicio 1: Realiza un programa que:
1. Crear un conjunto llamado usuarios con los usuarios Marta, David, Elvira, Juan y Marcos
2. Crear un conjunto llamado administradores Juan y Marta.
3. Borrar al administrador Juan del conjunto de administradores.
4. Añade a Marcos como nuevo administrador, pero sin borrarlo de usuarios.
5. Muestra todos los usuarios por pantalla de forma dinamica, ademas debe indicar cada usuario es admin o no'''

Usuarios = {
    "Marta",
    "David",
    "Elvira",
    "Juan",
    "Marcos"
}

Administradores = {
    "Juan",
    "Marta"
}

Administradores.discard("Juan")

Administradores.add("Marcos")

for usuario in Usuarios:
    if usuario in Administradores:
        print(f"El usuario {usuario} es administrador.")
    else:
        print(f"El usuario {usuario} no es administrador.")


'''Ejercicio 2: Durante el desarrollo de un pequeño videojuego se te encarga configurar y balancear cada clase de personaje jugable.
 Partiendo que la estadística base es 2, debes cumplir las siguientes condiciones:
 1. Los caballeros tiene el doble de vida y defensa que un guerrero.
 2. El guerrero tiene el doblo de ataque y alcance que un caballero.
 3. El arquero tiene la misma vida y ataque que un guerrero, pero la mitad de defensa y el doble de alcance.
 4. Muestra como quedan las propiedades de los tres personajes.'''

base = 2

personajes = {
    "caballero" : {
        "vida" : base * 2,
        "defensa" : base * 2,
        "ataque": base,
        "alcance": base 
    },
    "guerrero" :{
        "vida" : base,
        "defensa" : base,
        "ataque" : base * 2,
        "alcance" : base * 2
    },
    "arquero" :{
        "vida" : base,
        "defensa" : base / 2,
        "ataque" : base,
        "alcance": base * 4
    }
}

for personaje, caracteristicas in personajes.items():
    print(f"{personaje.capitalize()}")
    for clave, valor in caracteristicas.items():
        print(f"{clave} : {valor}")
    print()

'''Ejercicio 3: Durante la planificación de un proyecto se han acordado una lista de tareas. 
Para cada una de estas tareas se ha asignado un orden de prioridad (cuanto menor es el número de orden, más prioridad).'''

tareas = {
    "Tarea 1" : 3,
    "Tarea 2" : 1,
    "Tarea 3" : 4,
    "Tarea 4" : 2
}

tareas_ordenadas = sorted(tareas, key=tareas.get)

for tarea in tareas_ordenadas:
    print(f"{tarea} - Prioridad: {tareas[tarea]}")