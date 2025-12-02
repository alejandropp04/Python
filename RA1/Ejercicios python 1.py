#Calcula la suma de dos numeros
print("Ejercicio 1. Suma dos numeros")
num1 = 5
num2 = 6
suma = num1 + num2
print("La suma de {num1} + {num2} = {suma}")

# Calcular el area de un circulo
print("Ejercicio 2. Area circulo")
import math
diametro = float(input("Introduzca el radio del circulo: "))
circunferencia = diametro * math.pi
radio = diametro/2
print(f"La circunferencua es {circunferencia} y el radio es {radio}")

#Convertir grados Celsius a Farhenheit
print("Ejercicio 3. Celsius a Fahrenheit")
gradosC = float(input("Introduzca los grados en Celsius: "))
gradosf = (gradosC * 9/5) + 32

print(f"Grados convertidos a Fahrenheir {gradosf}")

#Calcular el doble y el triple de un numero
print("Ejercicio 4. Calcular doble y triple")
num = int(input("Introduzca un numero a convertir: "))
doble = int(num * 2)
triple = int(num * 3)
print(f"Doble de {num} = {doble}")
print(f"Triple de {num} = {triple}")

#Calcular la media de tres numeros
print("Ejercicio 5. Calcular la media de tres numeros")
numero1 = int(input("Introduzca el numero 1: "))
numero2 = int(input("Introduzca el numero 2: "))
numero3 = int(input("Introduzca el numero 3: "))

media = (numero1 + numero2 + numero3) / 3

print(f"La media de los tres numeros es: {media}")

#Multiplicar dos numeros
print("Ejercicio 6. Multiplicación")
multi1 = int(input("Introduzca un numero: "))
multi2 = int(input("Introduzca otro numero: "))
multi = multi1 * multi2
print(f"Resultado = {multi}")

#Concatenar dos cadenas de texto
print("Ejercicio 7. Concatenar dos cadenas")
cadena1 = "Que tal estas? "
cadena2 = "Bien y tu?"
resul = cadena1 + cadena2
print(resul)

#Mostrar un numero repetido varias veces
print("Ejericcio 8. Mostrar un numero repetido varias veces")
numero4 = 7
repeticiones = 6
print(str(numero4) * repeticiones)

#Calcular el área de un rectangulo
print("Ejercicio 9. Area del rectangulo")
base = 12
altura = 6
area = base * altura
print(f"Area del rectangulo: {area}")

#Calcular el perímetro de un rectangulo
print("Ejercicio 10. Calcular el perimetro del rectangulo")
base2 = 10
altura2 = 5
perimetro = 2 * (base*altura)
print(f"Perimetro del rectangulo: {perimetro}")