#Dos palabras y ver cual es mayor
word1 = "hello"
word2 = "world"
if word1 > word2:
    print(f"La palabra '{word1}' es mayor que la palabra '{word2}'")
elif word1 < word2:
    print(f"La palabra '{word2}' es mayor que la palabra '{word1}'")

#Cadenas
#Solo se pueden unir siendo del mismo tipo, no valido String int
str1 = "hello"
str2 = "there"
str3 = str1 + str2
print (str3) #Valido (hello there)

'''
str4  = 2
str3 = str2 + str4 
print (str3) Invalido, mezcla de caracteres '''

#Pedir cadena
name = input('Introduce tu nombre')
print (name)

'''Las cadenas reconocen el dato introducido como string, 
al igual que antes no se puede operar con ellas hay que transformarlo'''

apple = 100
#total = apple + name "Error"

num = input("introducza un numero")
num1 = int(num)
num2 = int(input("Introduzca un numero"))
suma = num1 + num2

print (suma)

'''Cadenas iterables por posiciones'''
string = "Estamos estudiando para el examen"

pos = string[5]
print (pos) #Devuelve la posicion 5

pos2_12 = string[2:12]
prim5 = string[0:5]
ultimas5 = string[-5:]

'''Si la cadena no tiene las posiciones mostrara un error por consola 
ya que no estaria en el rango'''

'''Longitud de la cadena'''
longitud = len(string)
print (longitud)

'''Recorrer una cadena con un bucle'''

marca = "mercedes"
i = 0
for i in range (len(marca)):
    letra = marca[i]
    print(f"{i}. {letra}")

'''Otro bucle for in'''
for letra in marca:
    print(letra)


'''Metodos de Strings'''
print(marca.capitalize())
#Minusculas
print(marca.lower())
#Mayusculas
print(marca.upper())

'''Centra el texto de una cadena de longitud width'''
print(marca.center(20))
#Opcional lo rellena con algun caracter
print(marca.center(20,"-"))

'''Finaliza la cadena'''
cadena = "Hola que tal"
print(cadena.endswith("tal")) #True

'''Busca en la cadena un texto y devuelve la posicion'''
print(cadena.find("que")) #5

'''Elimina los espacios de la cadena (del principio)'''
cadena2 = "   Hola que tal   "
print(cadena2.lstrip())
'''Elimina los espacios de la cadena (del final)'''
print(cadena2.rstrip())
'''Elimina los espacios de la cadena (de ambos lados)'''
print(cadena2.strip())

'''Reemplaza un texto por otro'''
print(cadena.replace("que", "como")) #En tercera posicion pone las veces Opcional

