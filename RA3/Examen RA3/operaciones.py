#Funcion mostrar y contar argumentos
def info_argumentos(*args):
    totalArgs = 0
    for argumento in args:
        totalArgs +=1
        print(argumento)
    print(f"Numero total de argumentos {totalArgs}")
    #Debe devolver el numero total de argumentos no imprimirlos

#Funcion argumentos divisibles entre 3
def divisibles3(*args):
    for argumento in args:
        if argumento % 3 == 0:
            print(f"El {argumento} es divisible entre 3")

#Funcion histograma, imprimir * por el valor de cada argumento
def histograma(*args):
    for argumento in args:
        print("*" * argumento)

#Funcion coste envio
def coste_envio(tarifa_base = 5, kilos = int, urgente = False):
    if(kilos <= 1):
        tarifa = tarifa_base
    elif(kilos > 1):
        tarifa = tarifa_base + (kilos*2)
    if(urgente):
        tarifa = tarifa + ((tarifa*30)/100)
    print(f"Importe total del envio {tarifa}")
    #Debe devolver el importe total del envio no imprimirlo
    #El precio debe estar en segunda o tercera posicion de la funcion, para no introducirlo siempre


#Funcion convertir a segundos
def convertir_segundos(horas, minutos, segundos):
    segundosTotales = (horas*3600) + (minutos*60) + segundos
    print(f"Total en segundos: {segundosTotales}")