#Abrimos un fichero
try:
    with open("fichero.txt", "r") as fichero:
        contenido = fichero.read()
        print(contenido)
except FileNotFoundError:
    print("El fichero no existe")

f = open("fichero.txt", "r")
print(f.read())
print(f.readline())

#Abrir el fichero con "write" -> "w"
with open("fichero.txt", "w") as fichero:
    fichero.write("Woops! He eliminado el contenido")

#Leemos el fichero
with open("fichero.txt") as f:
    print(f.read())