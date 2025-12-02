#Funcion "precioEntrada", necesita conocer el precio normal de la entrada
#Precio por defecto 10, edad del asistente y si es o no estudiante
#En caso de ser < 18 o estudiante descuento del 50%

def precioEntrada(precio = 10, edad = int, estudiante = bool):
    if edad < 18 or estudiante == True:
        return (precio - ((precio*50)/100))
    else:
        return precio

print(f"El precio de la entrada es: {precioEntrada(10, 20, False)}")