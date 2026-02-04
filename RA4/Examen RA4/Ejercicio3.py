facturas = {}
pendiente = 0
cobrada = 0
while True:
    accion = int(input("Seleccione '1' para añadir una factura, '2' para pagar una existente y '3' para terminar"))
    if accion == 1:
        clave = input("Introduzca el numero de la factura")
        valor = int(input(clave + "Introduzca el valor de la factura"))
        #Falta un IF para que no se añada al valor de la factura duplicada a "pendientes"
        facturas[clave] = valor
        pendiente += valor
        print(f"Cantidad cobrada: {cobrada} \nCantidad pendiente de cobro {pendiente}")
    if accion == 2:
        clave = input("Introduzca el numero de factura que desea pagar")
        if clave in facturas:
            cobrada += facturas[clave]
            pendiente -= facturas[clave]
            facturas.pop(clave)
            print(f"Cantidad cobrada: {cobrada} \nCantidad pendiente de cobro {pendiente}")    
        else:
            print("La factura seleccionada no se encuentra en el diccionario")
    if accion == 3:
        break