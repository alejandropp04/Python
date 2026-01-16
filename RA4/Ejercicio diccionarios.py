#Ejercicio listas con diccionarios
def diccionario_cadenas(cadena):
    diccionario = {
        "longitud" : len(cadena),
        "mayusculas" : cadena.upper(),
        "ultimas_cinco" : cadena[-5:]
    }
    return diccionario


cadena = input("Ingrese una cadena")

resultado = diccionario_cadenas(cadena)

for clave, valor in resultado.items():
    print(f"{clave}: {valor}")