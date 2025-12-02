#Importar las funciones de operaciones.py
import operaciones as operacion

#Ejecucion de la primera funcion
operacion.info_argumentos(2, 4, 5, 10, 15, 25)

#Ejecucion de la segunda funcion
operacion.divisibles3(3, 5, 6, 9)

#Ejecucion de la tercera funcion
operacion.histograma(4, 7, 9)


#Ejercicio 2
#Tarifa 10, 2 kilos y envio urgente
operacion.coste_envio(10, 2, True)

#Tarifa 5, 3 kilos, envio normal
operacion.coste_envio(5, 3)

#Tarifa 6, 0 kilos, envio normal
operacion.coste_envio(6, 0)

#Tarida 8, 0 kilos, envio urgente
operacion.coste_envio(8, 0, True)

#Ejercicio 3. Convertir a segundos
#Importar la funcion desde operaciones.py con el alias op
import operaciones as op
try:
    horas = int(input("Introduce las horas: "))
    if horas < 00 or horas >= 24 :
        raise ValueError ("Horas incorrectas. Rango de 00 a 23")
    minutos = int(input("Introduce los minutos: "))
    if minutos < 0 or minutos > 59:
        raise ValueError ("Minutos incorrectos. Rango de 0 a 59")
    segundos = int(input("Introduce los segundos: "))
    if segundos < 0 or segundos > 59:
        raise ValueError("Segundos no validos. Rango de 0 a 59")
    op.convertir_segundos(horas, minutos, segundos)
except ValueError as error:
    print(error)