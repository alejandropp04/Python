#Recorre la lista de nombres y los muestra
def nombres (*names):
    for name in names:
        print(name)
nombres ("Alex", "Pablo", "Antonio", "Juan")

#Recorre la lista de nombres y con greeting coge el nombre en la posicion 0
#Devuelve "Hola Carlos, Hola juan....."
def saludo (greeting, *nombres1):
    for nombre in nombres1:
        print(greeting, nombre)
saludo ("Hola", "Carlos", "Juan", "Sofia")

#Recorre la lista y muestra solo la posicion indicada
#En este caso se ha indicado la posicion 1, es decir "2"
def funcionN (*numeros):
    print(numeros[1])
funcionN (1, 2, 3, 4)

#Recorre la lista de numeros y devuelve el total
def my_function(*numbrers):
    total = 0
    for num in numbrers:
        total += num
    return total
print(my_function(10, 20, 30))

#Encontrar el valor mas alto
def func_max(*numbers):
    if len(numbers) == 0:
        return None
    max_num = numbers[0]
    for num in numbers:
        if(num > max_num):
            max_num = num
    return max_num
print(func_max (5, 3, 2, 1, 7))

#Multiplica por cada argumento y sume todo
def func_multi (operador, *numbers):
    total = 0
    for num in numbers:
        rdo = operador * num
        print(rdo)
        total += rdo
    print(f"Total de numeros multiplicados {total}")
print("----------")
func_multi(2, 3, 4, 5)

#Pizza, tamaño y ingredientes
def madePizza (porciones, *ingredientes):
    print(f"Pizza de {porciones} con los siguientes ingredientes: ")
    for ingrediente in ingredientes:
       print(ingrediente, end=", ")
madePizza(5, "bacon", "jamon", "pollo") #Con tamaño e ingredientes
print(" \n --------")

#Funcion ganador, devuelve "return" un ganador de forma aleatoria, (introduce varios nombres)
import random
def ganador(*nombres):
    return random.choice(nombres)
print(f"Ganador",ganador("Alex", "David", "Pablo", "Ana", "Carlos"))

#Funcion ganador sin random choice
import random

def ganador(*nombres):
    if(len(nombres) == 0):
        return("No hay datos en la lista")
    else:
        ganador = random.randint(0, len(nombres) -1)
        return(f"El ganador es: {nombres[ganador]}")
print(ganador("Ana", "Alex", "David"))