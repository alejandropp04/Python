#Ejercicio con switch

'''Crea un programa en Python que pida al usuario el nombre de una región (por ejemplo: 
    "Europa", "América", "Asia", "África" u "Oceania") y muestre en pantalla la zona horaria
    aproximada correspondiente a esa region. '''

#Pedir region
region = input("Introduce una región (Europa, America, Asia, Africa, Oceania)").strip().capitalize()

#Switch para las diferentes zonas horarias
match region:
    case "Europa":
        print("La zona horaria aproximada de Europa es UTC+1 a UTC+3")
    case "America":
        print("La zona horaria aproximada de América es UTC-3 a UTC-8")
    case "Asia":
        print("La zona horaria aproximada de Asia es UTC+5 a UTC+9")
    case "Africa":
        print("La zona horaria aproximada de África es UTC+0 a UTC+3")
    case "Oceania":
        print("La zona horaria aproximada de Oceania es UTC+10 a UTC+12")
    case _:
        print("Región no reconocida. Por favor, introduce una region valida")