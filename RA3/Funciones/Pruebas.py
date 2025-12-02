#Ejercicio 3: Adivina el numero
import random
aleatorio = random.randint(1, 100)
intentos = 0
while True:
    try:
        num = int(input("Introduzca un numero: "))
    except ValueError:
        print("Introduzca un numero entero")
        continue

    intentos += 1
    if(aleatorio == num):
        print(f"Has acertado el numero aleatorio. Intentos: {intentos}")
        break
    elif(aleatorio > num):
        print("El numero aleatorio es mayor")
    else:
        print("El numero aleatorio es menor")      
print("Programa finalizado")
