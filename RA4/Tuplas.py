mytuple = ("apple", "banana", "cherry")
print (mytuple)

#Imprimir el elemnto 1
print (mytuple[1])

#Las tuplas permiten duplicados
tuple = ("apple", "banana", "cherry", "apple")
print (tuple)

#Miramos si hay apple
if "apple" in tuple:
    print ("Yes, there is apple in tuple")

#Ejercicio con tuplas
#Haz dos funciones, saludar y despedir, una tupla con los dos elementos y que si
#coinciden con los elementos de la tupla ejecutar la funcion y sino que muestre
#que no se ha encontrado el elemento

def saludar():
    print ("Hola")
def despedir():
    print ("Adios")

tupla = ("saludar", "despedir")

elemento = input("Introduzca una palabra para ver si coincide con algun elemento de la tupla: ")

if elemento == tupla[0]:
    saludar()
elif elemento == tupla[1]:
    despedir()
else:
    print("No se ha encontrado ningun elemento identico")

#Contar los numeros impares que hay en una tupla con count
numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10)

pares = 0
impares = 0
i = 0
for i in range (1, 11):
    if i % 2 == 0:
        pares += numeros.count(i)
    else:
        impares += numeros.count(i)
print("Pares: ", pares)
print("Impares: ", impares)