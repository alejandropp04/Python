#Importar modulo de calculadora
import calcula

#Importamos con un alias
import calcula as c

#Importar directamente la funcion suma y resta, se puede solo importar una
from calcula import suma, resta

calcula.suma(5, 3) #Llamando a la funcion con el modulo

c.suma(4, 5) #Llamando a la funcion con el alias

suma(2, 2) #Llamando directamente a la funcion suma
resta(10, 5)
