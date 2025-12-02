#Ejercicio 1: Calculadora de inversion con funciones
def calculadora_inversion(inversion, interes, años):
    if inversion <= 0 or interes < 0 or años <= 0:
        print("Error: todos los valores deben ser positivos.")
        return

    total = inversion

    print("\nEvolución de la inversión:")
    for i in range(1, años + 1):
        total += total * (interes / 100)
        print(f"Año {i}: {total:.2f} €")

# Llamada a la función
calculadora_inversion(1000, 12, 10)

# Ejercicio 2: Cuenta atrás
def cuenta_atras(numero):
    if numero <= 0:
        print("Error: Introduzca un número entero positivo.")
        return  # salir de la función si no es válido

    for i in range(numero, 0, -1):
        print(i, end=", ")
    print("Fin del programa")

# Llamada a la función con parámetro
cuenta_atras(5)


#Ejercicio 3: Multiplos
def multiplos(inicio, fin):
    for numero in range(inicio, fin):
        if(numero % 7 != 0):
            continue
        print(f"El primer multiplo de 7 entre 80 y 200 es: {numero}")
        break

multiplos(81, 200)

#Ejercicio 4: Inventario
def gestionar_inventario():
    inventario = {"manzanas": 0, "peras": 0, "platanos": 0}

    while True:
        print("\n--- MENÚ FRUTERÍA ---")
        print("1. Añadir stock")
        print("2. Vender producto")
        print("3. Mostrar inventario")
        print("4. Salir")

        opcion = input("Seleccione una opción (1-4): ")

        if opcion == "1":  # Añadir stock
            producto = input("¿Qué producto quiere añadir (manzanas, peras, platanos)? ").lower()
            if producto in inventario:
                try:
                    cantidad = int(input("¿Cuántas unidades quiere añadir? "))
                    if cantidad > 0:
                        inventario[producto] += cantidad
                        print(f"Se añadieron {cantidad} {producto}.")
                    else:
                        print("Error: la cantidad debe ser positiva.")
                except ValueError:
                    print("Error: debe introducir un número válido.")
            else:
                print("Producto no reconocido.")

        elif opcion == "2":  # Vender producto
            producto = input("¿Qué producto quiere vender (manzanas, peras, platanos)? ").lower()
            if producto in inventario:
                try:
                    cantidad = int(input("¿Cuántas unidades quiere vender? "))
                    if 0 < cantidad <= inventario[producto]:
                        inventario[producto] -= cantidad
                        print(f"Se vendieron {cantidad} {producto}.")
                    elif cantidad > inventario[producto]:
                        print(f"No hay suficientes {producto} en el inventario.")
                    else:
                        print("Error: la cantidad debe ser positiva.")
                except ValueError:
                    print("Error: debe introducir un número válido.")
            else:
                print("Producto no reconocido.")

        elif opcion == "3":  # Mostrar inventario
            print("\nInventario actual:")
            for producto, cantidad in inventario.items():
                print(f"{producto.capitalize()}: {cantidad}")

        elif opcion == "4":  # Salir
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Elija una opción correcta (1-4).")

# Llamada a la función
gestionar_inventario()

#Ejericio 5: Montador de menu rapido
def elegir_plato():
    print("\n--- PLATOS PRINCIPALES ---")
    print("1. Pollo asado - 8.50€")
    print("2. Pasta carbonara - 7.50€")
    print("3. Ensalada mixta - 6.00€")

    opcion = int(input("Elige un plato (1-3): "))
    if opcion == 1:
        return "Pollo asado", 8.50
    elif opcion == 2:
        return "Pasta carbonara", 7.50
    elif opcion == 3:
        return "Ensalada mixta", 6.00
    else:
        print("Opción de plato no válida.")
        exit()


def elegir_bebida():
    print("\n--- BEBIDAS ---")
    print("1. Agua - 1.50€")
    print("2. Refresco - 2.00€")
    print("3. Cerveza - 2.50€")

    opcion = int(input("Elige una bebida (1-3): "))
    if opcion == 1:
        return "Agua", 1.50
    elif opcion == 2:
        return "Refresco", 2.00
    elif opcion == 3:
        return "Cerveza", 2.50
    else:
        print("Opción de bebida no válida.")
        exit()


def elegir_complemento():
    print("\n--- COMPLEMENTOS ---")
    print("1. Pan y alioli - 1.00€")
    print("2. Patatas fritas - 2.00€")
    print("3. Fruta del día - 1.50€")

    opcion = int(input("Elige un complemento (1-3): "))
    if opcion == 1:
        return "Pan y alioli", 1.00
    elif opcion == 2:
        return "Patatas fritas", 2.00
    elif opcion == 3:
        return "Fruta del día", 1.50
    else:
        print("Opción de complemento no válida.")
        exit()


def elegir_pago():
    print("\n--- MÉTODO DE PAGO ---")
    print("1. Efectivo")
    print("2. Tarjeta")

    opcion = int(input("Elige método de pago (1-2): "))
    if opcion == 1:
        return "Efectivo"
    elif opcion == 2:
        return "Tarjeta"
    else:
        print("Opción de pago no válida.")
        exit()


def mostrar_resumen(plato, precio_plato, bebida, precio_bebida, complemento, precio_complemento, metodo_pago):
    total = precio_plato + precio_bebida + precio_complemento
    print("\n--- RESUMEN DEL PEDIDO ---")
    print(f"Plato: {plato} - {precio_plato:.2f}€")
    print(f"Bebida: {bebida} - {precio_bebida:.2f}€")
    print(f"Complemento: {complemento} - {precio_complemento:.2f}€")
    print(f"Forma de pago: {metodo_pago}")
    print("---------------------------")
    print(f"TOTAL A PAGAR: {total:.2f}€")
    print("\nGracias por su pedido. Buen provecho.")


def main():
    print("Bienvenido al restaurante Pythonico")
    plato, precio_plato = elegir_plato()
    bebida, precio_bebida = elegir_bebida()
    complemento, precio_complemento = elegir_complemento()
    metodo_pago = elegir_pago()
    mostrar_resumen(plato, precio_plato, bebida, precio_bebida, complemento, precio_complemento, metodo_pago)


# Llamada principal
main()
