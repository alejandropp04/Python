#Ejercicio 1: Calculadora de operaciones basicas
while True:
    try:
        num1 = int(input("Introduzca un numero: "))
        num2 = int(input("Introduzca otro numero: "))
        
        operacion = int(input("Seleccione una opcion: \n 1.Suma \n 2.Resta \n 3.Multiplicacion \n 4.Division \n 5.Salir "))

        match(operacion):
            case 1:
                rdo = num1 + num2
                print(f"Resultado {num1} + {num2} = {rdo}")
            case 2:
                rdo = num1 - num2
                print(f"Resultado {num1} + {num2} - {rdo}")
            case 3:
                rdo = num1 * num2
                print(f"Resultado {num1} * {num2} = {rdo}")
            case 4:
                if(num2 < 0):
                    raise ZeroDivisionError("No se puede dividir entre 0")
                else:
                    rdo = num1 / num2
                    print(f"Resultado {num1} / {num2} = {rdo}")
            case 5:
                break
    except ValueError:
        print("Error: Debe introducir un valor numerico")
    except ZeroDivisionError as error:
        print(error)
print("Programa finalizado")

#Ejercicio 2: Tabla de multiplicar
try:
    num = int(input("Introduzca un numero para ver su tabla de multiplicar"))

    for operando in range(0, 11, 1):
        rdo = int(num * operando)
        print(f"{num} X {operando} = {rdo}")

except ValueError:
    print("Error: Debe introducir un numero")

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

#Ejercicio 4: Comprobar si un numero es primo
try:
    numero = int(input("Introduzca un numero para saber si es primo: "))

    esPrimo = True

    if(numero <= 1):
        print(f"El numero {numero} no es primo")

    for i in range(2, numero):
        if(numero % i == 0):
            esPrimo = False
            break
    
    if esPrimo:
        print(f"El numero {numero} es primo")
    else:
        print(f"El numero {numero} no es primo")

except ValueError:
    print("Error. Introduzca un numero entero positivo")

#Ejercicio 5: Numero primos hasta N
try:
    numero = int(input("Introduzca un numero para saber si es primo: "))

    if(numero <= 1):
        print(f"El numero {numero} no es primo")
    else:
        print(f"Numeros primos desde 2 hasta {numero}")

        for n in range (2, numero +1):
            esPrimo = True
            i = 2

            while i < n:
                if(n % i == 0):
                    esPrimo = False
                    break
                i += 1

            if esPrimo:
                print(n, end=" ")

except ValueError:
    print("Error. Introduzca un numero entero positivo")

#Ejercicio 6: Analisis de notas de alumnos //Variante sin pedir notas
notas = [5, 6, 7, 10, 9, 9, 4, 2]
aprobados = 0
total = 0
maxNota = notas[0]
minNota = notas[0]
for nota in notas:
    total += nota
    if(nota >= 5):
        aprobados += 1
    if(nota > maxNota):
        maxNota = nota
    if(nota < minNota):
        minNota = nota
media = total / len(notas)
print(f"Aprobados: {aprobados}")
print(f"Media del grupo: {media}")
print(f"Nota mas alta: {maxNota}, Nota mas baja {minNota}")

#Ejercicio 6: Analisis de notas de alumnos //Variante pidiendo notas
try:
    notas = []
    aprobados = 0
    total = 0
    alumnos = int(input("Introduzca el numero de alumnos: "))
    for i in range (alumnos):
        nota = int(input(f"Introduzca la nota del alumno {i}: "))
        notas.append(nota)
        total += notas[i]

        if(i == 0):
            maxNota = notas[0]
            minNota = notas[0]
        if(notas[i] >= 5):
            aprobados += 1
        if(notas[i] > maxNota):
            maxNota = notas[i]
        if(notas[i] < minNota):
            minNota = notas[i]
    media = total / alumnos
    print(f"Aprobados: {aprobados}")
    print(f"Madia de los alumnos: {media}")
    print(f"Max nota: {maxNota}. Min nota: {minNota}")
except ValueError:
    print("Introduzca un numero entero positivo")
