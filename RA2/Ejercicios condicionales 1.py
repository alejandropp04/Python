# Ejercicios condicionales

# Ejercicio 1: Verificacion de edad
try :
    edad = int(input("Introduzca su edad: "))
except ValueError:
    print("Caracter introducido no valido, introduzca un numero entero positivo")
    exit()

if edad < 18:
    print(f"Eres menor de edad")
else:
    print(f"Eres mayor de edad")

# Ejercicio 2: Comparacióm de dos números
try:
    num1 = int(input("Introduzca un numero: "))
    num2 = int(input("Introduzca otro numero: "))
    if(num1 > num2):
        print(f"El numero {num1} es  mayor que {num2}")
    elif(num2 > num1):
        print(f"El numero {num2} es mayor que {num1}")
    else:
        print(f"El numero {num1} es igual que {num2}")
except ValueError:
    print("ERROR: Introduzca un numero entero")
    exit()



#Ejercicio 3: Validacion de notas
try:
    nota = float(input("Introduzca una nota: "))
    
    if(nota < 0 or nota > 10):
        raise ValueError
    else:
        if(nota >= 0 and nota <= 4.9):
            print("suspenso")
        elif(nota >= 5 and nota <= 6.9):
            print("Aprobado")
        elif(nota >= 7 and nota <= 8.9):
            print("Notable")
        elif(nota >= 9 and nota <= 10):
            print("Sobresaliente")
except ValueError:
    print("Introduzca una nota valida entre 0 y 10")

    
#Ejercicio 4: Acceso con clave
try:
    clave = input("Introduce la clave: ")
    
    if clave != "python123":
        raise ValueError("Acceso denegado")
    else:
        print("Acceso concedido")

except ValueError as error:
    print(error)

#Ejercicio 5: Menu de seleccion
print("Menú de opciones:")
print("1. Ver perfil")
print("2. Editar perfil")
print("3. Salir")

try:
    opcion = int(input("Introduce el numero de la opción: "))

    match opcion:
        case 1:
            print("Mostrando perfil")
        case 2:
            print("Editando perfil")
        case 3:
            print("Saliendo")
        case _:
            raise ValueError("Opcion del menu no valida")
except ValueError:
    print(error)


#Ejericio 6: Validacion de un numero par o impar
try:
    num = int(input("Introduzca un numero"))
    if(num % 2 == 0):
        print(f"El numero {num} es par")
    else :
        print(f"El numero {num} es impar")
except ValueError:
    print("El numero introducido no es valido, introduzca un numero entero")

#Ejercicio 7: Verificacion de permisos de conducir segun la edad
try:
    edad = int(input("Introduce tu edad: "))

    if edad < 14:
        print("No puedes conducir")
    elif edad >= 18:
        print("Puedes conducir coche")
    elif edad >= 16:
        print("Puedes conducir moto de gran cilindrada")
    elif edad >= 14:
        print("Puedes conducir moto de poca cilindrada")

except ValueError:
    print("Error: Debes introducir un número válido")
