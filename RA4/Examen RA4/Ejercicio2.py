lista = ["Hacer ejercicios de Python", "Estudiar cliente", "Aprender ingles", "Aprobar java", "Proyecto de digitalizacion", "Examen de conducir", "Lavar los platos", "Estudiar frances"]

def mostrar_tareas():
    for tarea in lista:
        print(tarea)

def insertar_tarea(nombre, posicion):
    lista.insert(posicion-1, nombre)
    print(f"Tarea añadida en la posicion {posicion}")

def eliminar_tarea(nombre):
    if nombre in lista:
        lista.remove(nombre)
        print(f"Tarea {nombre} eliminada")
    else:
        print(f"La tarea no se encuentra en la lista")

def mover_tarea(nombre, posicion):
    if nombre in lista:
        lista.remove(nombre)
        lista.insert(posicion-1, nombre)
        print(f"Tarea movida a la posicion {posicion}")
    else:
        print("La tarea no se encuentra en la lista")


mostrar_tareas()        
insertar_tarea("Ir a entrenar", 2)
eliminar_tarea("Estudiar cliente")
mover_tarea("Aprobar java", 1)
mostrar_tareas()