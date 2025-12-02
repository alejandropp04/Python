#Ejercicio 1: Calculadora de inversion
try:
    inversion = float(input("Cantidad a invertir: "))
    interes = float(input("Interes anual: "))
    años = int(input("Años de la inversion: "))
    total = inversion
    for i in range (1, años + 1):
        total += total * (interes /100)
        print(f"Año {i}: {total:.2f} €")
except ValueError:
    print("Introduzca un numero positivo")

#Ejercicio 2: Cuenta atras
try:
    numero = int(input("Introduzca un numero para la cuenta atras: "))
    for i in range(numero, 0, -1):
        print(i, end=", ")
    print("fin del programa")
except ValueError:
    print("Error, Introduzca un numero entero positivo")

#Ejercicio 3: Multiplos
for numero in range(81, 200):
    if(numero % 7 != 0):
        continue
    print(f"El primer multiplo de 7 entre 80 y 200 es: {numero}")
    break

#Ejercicio 4: Inventario
inventario = {"manzanas": 0, "peras": 0, "platanmos":0}

while True:
    print("\n--- MENÚ FRUTERÍA ---")
    print("1. Añadir stock")
    print("2. Vender producto")
    print("3. Mostrar inventario")
    print("4. Salir")

    opcion = input("Seleccione una opcion (1-4)")

    if opcion == "1": #Añadir stock
        producto = input("¿Que producto quiere añadir (manzanas, peras, platanos?").lower
        if producto in inventario:
            try:
                cantidad = int(input("¿Cuantas cantidades quieres añadir?"))
                if cantidad > 0:
                    inventario[producto] += cantidad
                    print(f"Se añadieron {cantidad} {producto}")
                else:
                    print("Error. La cantidad ebe ser positiva")
            except ValueError:
                print("Error. Debe introducir un numero valido")
        else:
            print("Producto no reconocido")
    elif opcion == "2": #Vender producto
        producto = input("¿Que producto quiere vender (manzanas, peras, platanos)")
        if producto in inventario:
            try:
                cantidad = int(input("¿Cuantas unidades quiere vender?"))
                if 0 < cantidad <= inventario[producto]:
                    inventario[producto] -= cantidad
                    print(f"Se vendieron {cantidad} {producto}")
                elif cantidad > inventario[producto]:
                    print(f"No hay suficientes {producto}")
                else:
                    print("La cantidad debe ser positiva")
            except ValueError:
                print("Debes introducir un numero valido")
        else:
            print("Producto no reconocido")
    
    elif opcion == "3": #Mostrar inventario
        print("Inventario actual")
        for producto, cantidad in inventario.items():
            print(f"{producto.capitalize()}: {cantidad}")
        
    elif opcion == "4":
        print("Saliendo del programa")
    
    else:
        print("Opcion no valida, elige una opcion correcta (1-4)")

# Ejercicio 4: Inventario (versión con variables simples)
manzanas = 0
peras = 0
platanos = 0

while True:
    print("\n--- MENÚ FRUTERÍA ---")
    print("1. Añadir stock")
    print("2. Vender producto")
    print("3. Mostrar inventario")
    print("4. Salir")

    opcion = input("Seleccione una opción (1-4): ")

    if opcion == "1":  # Añadir stock
        producto = input("¿Qué producto quiere añadir (manzanas, peras, platanos)? ").lower()
        try:
            cantidad = int(input("¿Cuántas unidades quiere añadir? "))
            if cantidad <= 0:
                print("⚠️ La cantidad debe ser positiva.")
                continue
        except ValueError:
            print("⚠️ Debe introducir un número válido.")
            continue

        if producto == "manzanas":
            manzanas += cantidad
        elif producto == "peras":
            peras += cantidad
        elif producto == "platanos":
            platanos += cantidad
        else:
            print("⚠️ Producto no reconocido.")
            continue

        print(f"✅ Se añadieron {cantidad} {producto}.")

    elif opcion == "2":  # Vender producto
        producto = input("¿Qué producto quiere vender (manzanas, peras, platanos)? ").lower()
        try:
            cantidad = int(input("¿Cuántas unidades quiere vender? "))
            if cantidad <= 0:
                print("⚠️ La cantidad debe ser positiva.")
                continue
        except ValueError:
            print("⚠️ Debe introducir un número válido.")
            continue

        if producto == "manzanas":
            if cantidad <= manzanas:
                manzanas -= cantidad
                print(f"✅ Se vendieron {cantidad} {producto}.")
            else:
                print("⚠️ No hay suficientes manzanas.")
        elif producto == "peras":
            if cantidad <= peras:
                peras -= cantidad
                print(f"✅ Se vendieron {cantidad} {producto}.")
            else:
                print("⚠️ No hay suficientes peras.")
        elif producto == "platanos":
            if cantidad <= platanos:
                platanos -= cantidad
                print(f"✅ Se vendieron {cantidad} {producto}.")
            else:
                print("⚠️ No hay suficientes plátanos.")
        else:
            print("⚠️ Producto no reconocido.")

    elif opcion == "3":  # Mostrar inventario
        print("\n--- Inventario actual ---")
        print(f"Manzanas: {manzanas}")
        print(f"Peras: {peras}")
        print(f"Plátanos: {platanos}")

    elif opcion == "4":  # Salir
        print("👋 Saliendo del programa. ¡Hasta luego!")
        break

    else:
        print("⚠️ Opción no válida. Por favor, elija una opción entre 1 y 4.")

#Ejercicio 5: Montador de menu rapido
# Programa: Pedido de menú completo

print("🍽️ Bienvenido al restaurante Pythonico 🍽️")

# --- 1️⃣ Elegir plato ---
print("\n--- PLATOS PRINCIPALES ---")
print("1. Pollo asado - 8.50€")
print("2. Pasta carbonara - 7.50€")
print("3. Ensalada mixta - 6.00€")

plato_opcion = int(input("Elige un plato (1-3): "))

if plato_opcion == 1:
    plato = "Pollo asado"
    precio_plato = 8.50
elif plato_opcion == 2:
    plato = "Pasta carbonara"
    precio_plato = 7.50
elif plato_opcion == 3:
    plato = "Ensalada mixta"
    precio_plato = 6.00
else:
    print("⚠️ Opción de plato no válida.")
    exit()

# --- 2️⃣ Elegir bebida ---
print("\n--- BEBIDAS ---")
print("1. Agua - 1.50€")
print("2. Refresco - 2.00€")
print("3. Cerveza - 2.50€")

bebida_opcion = int(input("Elige una bebida (1-3): "))

if bebida_opcion == 1:
    bebida = "Agua"
    precio_bebida = 1.50
elif bebida_opcion == 2:
    bebida = "Refresco"
    precio_bebida = 2.00
elif bebida_opcion == 3:
    bebida = "Cerveza"
    precio_bebida = 2.50
else:
    print("⚠️ Opción de bebida no válida.")
    exit()

# --- 3️⃣ Elegir complemento ---
print("\n--- COMPLEMENTOS ---")
print("1. Pan y alioli - 1.00€")
print("2. Patatas fritas - 2.00€")
print("3. Fruta del día - 1.50€")

complemento_opcion = int(input("Elige un complemento (1-3): "))

if complemento_opcion == 1:
    complemento = "Pan y alioli"
    precio_complemento = 1.00
elif complemento_opcion == 2:
    complemento = "Patatas fritas"
    precio_complemento = 2.00
elif complemento_opcion == 3:
    complemento = "Fruta del día"
    precio_complemento = 1.50
else:
    print("⚠️ Opción de complemento no válida.")
    exit()

# --- 4️⃣ Método de pago ---
print("\n--- MÉTODO DE PAGO ---")
print("1. Efectivo")
print("2. Tarjeta")

pago_opcion = int(input("Elige método de pago (1-2): "))

if pago_opcion == 1:
    metodo_pago = "Efectivo"
elif pago_opcion == 2:
    metodo_pago = "Tarjeta"
else:
    print("⚠️ Opción de pago no válida.")
    exit()

# --- 5️⃣ Mostrar resumen del pedido ---
total = precio_plato + precio_bebida + precio_complemento

print("\n--- 🧾 RESUMEN DEL PEDIDO ---")
print(f"Plato: {plato} - {precio_plato:.2f}€")
print(f"Bebida: {bebida} - {precio_bebida:.2f}€")
print(f"Complemento: {complemento} - {precio_complemento:.2f}€")
print(f"Forma de pago: {metodo_pago}")
print("---------------------------")
print(f"TOTAL A PAGAR: {total:.2f}€")
print("\n✅ ¡Gracias por su pedido! ¡Buen provecho! 🍽️")