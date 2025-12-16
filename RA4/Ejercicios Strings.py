#Ejercicio 1: Modifica la cadena “               este ejercicio es muy complicado            ” 
# para que el ejercicio sea facilísimo  y cada una de las palabras comience en mayúsculas y 
# sin espacios y luego imprimelo invertido, ademas busca el indice de la palabra complicado.

cadena = "               este ejercicio es muy complicado            "
# Eliminar espacios al inicio y al final
cadena = cadena.strip()
# Buscar el índice de la palabra "complicado"
indice = cadena.find("complicado")
# Reemplazar "complicado" por "facil"
cadena = cadena.replace("complicado", "facil")
# Convertir cada palabra a mayúscula
cadena = cadena.title()
# Invertir la cadena
cadena_invertida = cadena[::-1]
# Mostrar la cadena invertida
print(cadena_invertida)
print(f"El índice de la palabra 'Complicado' es: {indice}")

#Ejercicio 2: Vamos a definir una cadena y la vamos a pasar a minusculas, eliminar los espacios
# y las letras pares las vamos a cambiar por asteriscos.
cadena2 = "  Python es un lenguaje de programacion genial   "
#Convertir a minusculas y eliminar espacios
cadena2 = cadena2.lower().replace(" ", "")
#Cambiar letras pares por asteriscos
nuevaCadena = ""
for i in range(len(cadena2)):
    if i % 2 == 0:
        nuevaCadena += cadena2[i]
    else:
        nuevaCadena += '*'
print(nuevaCadena)


#Ejercicio 4: A traves de una funcion que reciba un string y compruebe si todos los caracteres
# son mayúsculas
def es_mayusculas(cadena):
    return cadena.isupper()

# Ejecucion
cadena3 = "ESTA ES UNA CADENA EN MAYUSCULAS"
print(es_mayusculas(cadena3))
cadena4 = "Esta No Es Una Cadena En Mayusculas"
print(es_mayusculas(cadena4))