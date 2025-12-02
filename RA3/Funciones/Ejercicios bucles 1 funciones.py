#Ejercicio 1: Calculadora de operaciones básicas con funciones
def ejercicio_1():
    def calculadora():
        num1 = int(input("Ingrese el primer número: "))
        num2 = int(input("Ingrese el segundo número: "))
        operacion = int(input("Ingrese la operación (1=suma, 2=resta, 3=multiplicación, 4=división): "))

        match operacion:
            case 1:
                def suma(num1, num2):
                    return num1 + num2
                print(f'La suma de {num1} + {num2} = {suma(num1, num2)}')
            case 2:
                def resta(num1, num2):
                    return num1 - num2
                print(f'La resta de {num1} - {num2} = {resta(num1, num2)}')
            case 3:
                def multiplicacion(num1, num2):
                    return num1 * num2
                print(f'La multiplicación de {num1} * {num2} = {multiplicacion(num1, num2)}')
            case 4:
                def division(num1, num2):
                    if num2 == 0:
                        raise ZeroDivisionError("No se puede dividir entre 0")
                    return num1 / num2
                print(f'La división de {num1} / {num2} = {division(num1, num2)}')
            case _:
                raise ValueError("Operación no válida. Use 1..4")

    print("--- Ejercicio 1. Calculadora ---")
    try:
        calculadora()
    except Exception as e:
        print("Error calculadora:", e)

def ejercicio_2():
    #Ejercicio 2: Tabla de multiplicar
    num = int(input("Ingrese un número para la tabla de multiplicar: "))
    def tabla(num):
        resultados = []
        for i in range(11):
            rdo = num  * i
            resultados.append(rdo)
        return resultados

    print("\n--- Ejercicio 2. Tabla_multiplicar ---")
    print(*tabla(num, sep="\n"))

def ejercicio_3():
    #Ejercicio 3: Adivina el numero
    def verificar_adivina():
        import random
        aleatorio = random.randint(1, 100)
        intentos = 0

        while True:
            try:
                num = int(input("Introduzca un numero: "))
            except ValueError:
                print("Error. introduzca un numero entero")
                continue
            intentos+=1
            if(num > aleatorio):
                print("Numero secreto es mas pequeño")
            elif (num < aleatorio):
                print("Numero secreto es mas mayor")
            else:
                print(f"Has adivinado el numero aleatorio: {aleatorio}, en {intentos} intentos")
                break
    print("\n--- Ejercicio 3. Adivina el nimero aleatorio ---")
    verificar_adivina()

def ejercicio_4():
    #Ejercicio 4: comprobar si un numero es primo
    numero = int(input("Ingrese un número para comprobar si es primo: "))
    def es_primo(numero):
        if numero <= 1:
            return False

        for i in range(2, int(numero ** 0.5) + 1):
            if numero % i == 0:
                return False
        return True

    print("\n---  Ejercicio 4. es_primo ---")
    print(f"¿El numero {numero} es primo? {es_primo(numero)}")

def ejercicio_5():
    #Ejercicio 5: Numeros primos hasta N
    def primos_hasta_n(numero):
        try:
            numero = int(input("Introduzca un numero para saber sus primos anteriores"))
        except ValueError:
            print("Error. Introduzca un numero valido (int)")
        """Devuelve una lista con los números primos desde 2 hasta 'numero' (inclusive)."""
        if numero <= 1:
            return []
        primos = []
        for n in range(2, numero + 1):
            es_p = True
            for i in range(2, int(n ** 0.5) + 1):
                if n % i == 0:
                    es_p = False
                    break
            if es_p:
                primos.append(n)
        return primos
    print(primos_hasta_n())

#Ejericio 6: Analisis de notas de alumnos
def ejercicio_6():
    print("\n -- Ejercicio 6. Analizar notas ---")
    alumnos = int(input("Ingrese el número de alumnos: "))
    notas = []
    for i in range(alumnos):
        nota = float(input(f"Ingrese la nota del alumno {i + 1}: "))
        notas.append(nota)
    def aprobado(notas):
        aprobados = 0
        for nota in notas:
            if nota >= 5: aprobados += 1
        return aprobados
    print(f"Aprobados: {aprobado(notas)}")

# Ejecucion de ejercicios
#ejercicio_1()
#ejercicio_2()
ejercicio_3()
#ejercicio_4()
#ejercicio_5()
#ejercicio_6()