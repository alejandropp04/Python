#Ejercicios condicionales 2

#Ejercicio 1: Verificacion de numero primo
try:
    num = int(input("Introduzca un numero"))

    if(num <= 0):
        raise ValueError("El nuumero debe ser positivo")
    
    if(num == 1):
        print("1 no es primo, solo tiene un divisor")
    else:
        esPrimo = True
        divisor = None

        for i in range(2, int(num**0.5) + 1):
            if(num % i == 0):
                esPrimo = False
                divisor = i
                break
        if esPrimo:
            print(f"El numero {num} es primo")
        else:
            print(f"el numero {num} no es primo porque es divisible por {divisor}")
except ValueError as error:
    print(error)

#Ejercicio 2: Conversor entre divisa
tasas_cambio = {
    "USD": 1.10,  
    "GBP": 0.85,
    "JPY": 145.0
}

try:
    euros = float(input("Introduce la cantidad en euros: "))
    
    if euros <= 0:
        raise ValueError("La cantidad debe ser un número positivo.")
    
    divisa = input("Introduce la divisa destino (USD, GBP, JPY): ").upper()
    
    if divisa not in tasas_cambio:
        raise ValueError("Divisa no válida. Debe ser USD, GBP o JPY.")

    resultado = euros * tasas_cambio[divisa]
    
    print(f"{euros} EUR son {resultado:.2f} {divisa}")

except ValueError as e:
    print(f"Error: {e}")
except Exception:
    print("Ha ocurrido un error inesperado. Por favor, introduce datos correctos.")

#Ejercicio 3: Cálculo de raices reales de una ecuacion cuadratica
import math

try:
    a = float(input("Introduce el coeficiente a (no puede ser 0): "))
    if a == 0:
        raise ValueError("El coeficiente 'a' no puede ser 0. No es una ecuación cuadrática.")
    
    b = float(input("Introduce el coeficiente b: "))
    c = float(input("Introduce el coeficiente c: "))

    # Calcular discriminante
    D = b**2 - 4*a*c

    if D < 0:
        raise ValueError("No hay raíces reales, el discriminante es negativo.")

    # Calcular raíces
    raiz1 = (-b + math.sqrt(D)) / (2*a)
    raiz2 = (-b - math.sqrt(D)) / (2*a)

    # Mostrar resultados
    if raiz1 == raiz2:
        print(f"La ecuación tiene una raíz real: {raiz1}")
    else:
        print(f"La ecuación tiene dos raíces reales: {raiz1} y {raiz2}")

except ValueError as e:
    print(f"Error: {e}")
except Exception:
    print("Ha ocurrido un error inesperado. Por favor, revisa los datos introducidos.")

    
#Ejercicio 4: Simulador de cajero automatico
try:
    saldo = int(input("Introduzca el saldo de su cuenta: "))
    retiro = int(input("Introduzca la cantidad a retirar: "))

    if(saldo < 0 or retiro < 0):
        raise ValueError("El saldo y el retiro debe ser superior a 0")
    
    #Verificar que el retiro sea inferior al saldo
    if(retiro > saldo):
        raise ValueError("No cuenta con saldo suficiente para este retiro")
    

    if(saldo - retiro > 0):
        print(f"Cantidad a retirar: {retiro}")
        print(f"Saldo restante {saldo-retiro}")

except ValueError as error:
    print(error)


#Ejercicio 5: Calculadora de operaciones
try:
    num1 = float(input("Introduce el primer número: "))
    num2 = float(input("Introduce el segundo número: "))

    operacion = input("Introduce la operación (+, -, *, /): ")

    # Usamos match-case para seleccionar la operación
    match operacion:
        case "+":
            resultado = num1 + num2
        case "-":
            resultado = num1 - num2
        case "*":
            resultado = num1 * num2
        case "/":
            try:
                resultado = num1 / num2
            except ZeroDivisionError:
                print("Error: División por cero no permitida.")
                resultado = None
        case _:
            print("Error: Operación no reconocida.")
            resultado = None

    # Mostrar resultado si es válido
    if resultado is not None:
        print(f"El resultado de {num1} {operacion} {num2} es {resultado}")

except ValueError:
    print("Error: Debes introducir un número válido.")
except Exception:
    print("Ha ocurrido un error inesperado.")