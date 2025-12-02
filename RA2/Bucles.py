#Ejercicio 1: Haz un bucle que cuando introduzca un numero negativo
# se salga del bucle y si es igual a 0 que continue sin mostrar el numero
while(True):
    num = int(input("Introduzca un numero: "))
    if(num < 0):
        print("Numero negativo introducido. Fin del programa")
        break
    elif (num == 0):
        continue
    else:
        print("Numero : ", num)

#Ejercicio 2: Calcular la media de las notas (6 asignaturas)
notas = [7, 8, 9, 6, 7, 5]
total = 0
asignaturas = 0
for nota in notas:
    total += nota
    asignaturas += 1
media = total / asignaturas
print (f"Media : {media}")