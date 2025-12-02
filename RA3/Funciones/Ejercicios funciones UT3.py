# Ejercicio 1: Saludo personalizado
def ejercicio1():
    print("Ejercicio 1:")
    def saludar(saludo="Hola", nombre="Usuario"):
        return f"{saludo}, {nombre}!"
    
    # Ejecucion
    print(saludar())
    print(saludar(saludo="Buenos dias", nombre="Alex"))

# Ejercicio 2: Calculo de precio con IVA
def ejercicio2():
    print("Ejercicio 2:")
    def calcular_precio(precio_base=0.0, iva=21):
        precio_final = precio_base * (1 + iva / 100)
        return round(precio_final, 2)
    
    # Ejecucion
    print(calcular_precio())
    print(calcular_precio(200, iva=10))

# Ejercicio 3: Crear usuario con lista
def ejercicio3():
    print("Ejercicio 3:")
    def crear_usuario(nombre="Desconocido", email="sin_email@ejemplo.com", activo=True):
        if activo:
            return [nombre, email, activo]
        else:
            return []
    
    # Ejecucion
    print(crear_usuario())
    print(crear_usuario(nombre="Juan", email="juan@mail.com", activo=False)) #No lo creara ya que no esta activo
    print(crear_usuario(nombre="Juan", email="juan@mail.com", activo=True))

# Ejercicio 4: Formatear nombre completo
def ejercicio4():
    print("Ejercicio 4:")
    def formatear_nombre(nombre="SinNombre", apellido="SinApellido", orden="nombre_apellido"):
        if orden == "apellido_nombre":
            return f"{apellido} {nombre}"
        else:
            return f"{nombre} {apellido}"
    
    # Ejecucion
    print(formatear_nombre())
    print(formatear_nombre(nombre="Alex", apellido="Pacheco", orden="apellido_nombre")) #Primero apellido y luego el nombre
    print(formatear_nombre(nombre="Alex", apellido="Pacheco", orden="nombre_apellido"))

# Ejercicio 5: Calcular descuento
def ejercicio5():
    print("Ejercicio 5:")
    def calcular_descuento(precio_original=0.0, descuento=10):
        precio_final = precio_original * (1 - descuento / 100)
        return round(precio_final, 2)
    
    # Ejecucion
    print(calcular_descuento())
    print(calcular_descuento(200, descuento=25))

# Ejercicio 7: Filtrar números pares
def ejercicio7():
    print("Ejercicio 7:")
    def filtrar_pares(numeros=None):
        if numeros is None:
            numeros = []
            resultado = []
        else:
            for num in numeros:
                if num % 2 == 0:
                    resultado.append(n)
        return resultado    
    # Ejecucion
    print(filtrar_pares())
    print(filtrar_pares([1, 2, 3, 4, 5, 6, 7]))

# Ejercicio 8: Generar tabla de multiplica
def ejercicio8():
    print("Ejercicio 8:")
    def tabla_multiplicar(numero=1, hasta=10):
        return [f"{numero} x {i} = {numero * i}" for i in range(1, hasta + 1)]
    
    # Ejecucion
    print("\n".join(tabla_multiplicar()))
    print()
    print("\n".join(tabla_multiplicar(5, hasta=12)))

# Ejecuccion de los ejercicios:
#ejercicio1()
#ejercicio2()
#ejercicio3()
#ejercicio4()
#ejercicio5()
ejercicio7()
#ejercicio8()