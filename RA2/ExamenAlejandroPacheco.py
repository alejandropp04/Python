#Ejercicio 1: Lista de nombres
lista1 = ["carlos", "juan", "alejandro", "infanta"]
lista2 = ["fernandez", "perez", "elena", "carlos"]
combinaciones = 0

for i in range(0, len(lista1), 1):
    for f in range(0, len(lista2), 1):
        try:
            nombre = lista1[i] + " " + lista2[f]
            print(nombre)
            combinaciones +=1
            if(lista1[i] == "infanta" and lista2[f] == "elena"):
                raise ValueError("IES en Galapagar con estudios en formación profesional")
            if(lista1[i] == lista2[f]):
                combinaciones -=1
                raise ValueError("No se pueden crear un nombre compuesto a partir de dos nombres iguales")
        except ValueError as error:
            print (error)
            continue
print(f"Combinaciones de nombres validas creadas {combinaciones}")


#Ejercicio 2: Precios
productos = []
total = 0
precios10 = 0
precioMax = 0

while True:
    try:
        precio = float(input("Introduzca el precio del producto: "))
        
        if(precio < 0):
            raise ValueError("Error. Debe introducir un numero mayor o igual que cero")
        if(precio >= 10 and precio != 9999.99):
            total += precio
            precios10 += 1
            if(precio > precioMax):
                precioMax = precio
            productos.append(precio)
        elif(precio == 9999.99):
            break
    except ValueError as e:
        print(e)
        continue


for producto in productos:
    print(producto)

#Calcular el precio medio
pmedio = total / precios10

print(f"Productos mayores a 10 euros: {precios10}")
print(f"Precio medio de los productos: {pmedio}")
print(f"Precio mas alto: {precioMax}")
        
#Ejercicio 3: Fibonacci
num1 = 0
num2 = 1
fibonacci = num1
for i in range(0, 10, 1):
    print(fibonacci, end=", ")
    num1 = num2
    num2 = fibonacci
    fibonacci = num1 + fibonacci