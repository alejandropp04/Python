#Ejercicio salacio con funciones
def salario(hours, rate):
    if (hours > 40):
        hoursE = hours - 40
        rateE = rate * 1.5
        pay = ((40 * rate) + (hoursE * rateE))
        return pay
    else:
        pay = hours * rate
        return pay

try: 
    horas = float(input("Introduzca las horas trabajadas a la semana: "))
    salarioHora = float(input("Introduzca su salario por hora: "))
    print(f"Pago a recibir: {salario(horas, salarioHora):.2f}")
except ValueError:
    print("Introduzca el salario y las horas válidas.")

#Ejercicio calificacion
def calificacion(score):
    if score >= 0.9:
        return "A"
    elif score >= 0.8:
        return "B"
    elif score >= 0.7:
        return "C"
    elif score >= 0.6:
        return "D"
    else:
        return "F"
try:
    nota = float(input("Introduzca la nota (entre 0.0 y 1.0): "))
    if 0.0 <= nota <= 1.0:
        print(f"Su calificación es: {calificacion(nota)}")
    else:
        print("Error: La nota debe estar entre 0.0 y 1.0.")
except ValueError:
    print("Error: Debe introducir un número válido.")