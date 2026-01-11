#Ejercicio listas.
#Haz un switch que de las opciones:
#1- Añadir elementos a una lista
#2- Modificar elementos 2 al 4 de la lista
#3- Eliminar el último elemento de la lista
#4- Mostrar la lista
#5- Salir

def ejercicio_listas():
    lista = []

    while True:
        print("\nOpciones:")
        print("1- Añadir elementos a una lista")
        print("2- Modificar elementos 2 al 4 de la lista")
        print("3- Eliminar el último elemento de la lista")
        print("4- Mostrar la lista")
        print("5- Salir")

        opcion = input("Selecciona una opción (1-5): ")

        match opcion:
            case '1':
                elemento = input("Introduce el elemento a añadir: ")
                lista.append(elemento)
                return lista

            case '2':
                for i in range(1, 4):
                    if i < len(lista):
                        nuevo_valor = input(
                            f"Introduce el nuevo valor para el elemento en la posición {i} (actual: {lista[i]}): "
                        )
                        lista[i] = nuevo_valor
                return lista

            case '3':
                if lista:
                    lista.pop()
                return lista

            case '4':
                return lista

            case '5':
                return lista

            case _:
                print("Opción no válida")
# Prueba del ejercicio
resultado = ejercicio_listas()
print("Lista final:", resultado)