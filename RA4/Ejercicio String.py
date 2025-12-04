#A traves de una funcion, introduciendo un string por parametro, devolver la longitud, mostrar la cadena en minuscular y las 5 ultimas letras
def procesar_cadena(cadena):
    longitud = len(cadena)
    minusculas = cadena.lower()
    ultimas_cinco = cadena[-5:]
    return f"La cadena tiene {longitud} letras, en minusculas es '{minusculas}', y las 5 ultimas letras son '{ultimas_cinco}'"

#Ejemplo de uso
cadena = "Hola buenas tardes"
print(procesar_cadena(cadena))