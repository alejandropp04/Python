#Calcular la media de tres numeros
print("Ejercicio 5. Calcular la media de tres numeros")
numero1 = int(input("Introduzca la primera nota: "))
numero2 = int(input("Introduzca la segunda nota: "))
numero3 = int(input("Introduzca la tercera nota: "))
        
if numero1 < 0 or numero2 < 0 or numero3 < 0 :
    print("El numero no es valido")
elif numero1 > 10 or numero2 > 10 or numero3 > 10:
    print("El numero no es valido")
else:
    media = (numero1 + numero2 + numero3) / 3
    print(f"Nota media es: {media}")
    if(media > 5):
        print("Has aprobado")
    else:
        print("Has suspendido")
print("El programa ha finalizado")