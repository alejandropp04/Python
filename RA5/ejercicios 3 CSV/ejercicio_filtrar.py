#Escribe un progrmaa que lea un archivo CSV llamado empleados.csv y
#muestre solo a los empleados que tengan un salario superior a 3000, meterlo en un nuevo archivo
import csv

with open("empleados.csv", "r") as f:
    lector = csv.DictReader(f)
    empleadores_filtrados = [linea for linea in lector if float(linea["Salario"]) > 3000]
    with open("empleados_filtrados.csv", "w") as f_filtrado:
        escritor = csv.DictWriter(f_filtrado, fieldnames=lector.fieldnames)
        escritor.writeheader()
        escritor.writerows(empleadores_filtrados)

#Ademas mostrar por pantalla el sueldo promedio de los empleados filtrados
total_salarios = sum(float(empleado["Salario"]) for empleado in empleadores_filtrados)
contador_empleados = len(empleadores_filtrados)
if contador_empleados > 0:
    salario_promedio = total_salarios / contador_empleados
    print(f"Salario promedio de los empleados filtrados: {salario_promedio:.2f}")
else:
    print("No hay empleados con salario superior a 3000.")