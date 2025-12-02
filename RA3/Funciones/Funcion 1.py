#Funcion 1: Verificar mayor de edad
def funcion(edad):
    if edad >= 18:
        print("Eres mayor de edad.")
    else:
        print("Eres menor de edad.")
funcion(20)

#Funcion 2: Saludo simple
def saludo():
    print("Hola, bienvenido/a!")
saludo()

#Funcion 3: Saludo con nombre
def saludo2(nombre):
    print(f"Hola, {nombre}, bienvenido/a!")
saludo2("Alejandro")

#Funcion 4: Devolver un valor
def suma(a, b):
    return a + b
print(f"El resultado de la suma es: {suma(5, 3)}")