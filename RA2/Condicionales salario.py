horas = input("Introduzca las horas trabajadas: ")
salario = input("Introduzca el salario por hora: ")

try:
    horasT = int (horas)
    salarioH = int (salario)
    if(horasT>40):
        horasExtra = horasT - 40
        salarioExtra = salarioH * 1.5
        pago = (horasT - horasExtra) * salarioH + horasExtra * salarioExtra
    else:
        pago = horas * salario
    print("Salario a percibir: ", pago)
except:
    print("Error, por favor introduzca un valor numerico")

