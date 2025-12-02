#funcion recursiva
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

#Ejemplo
print("El factorial de 5 es:", factorial(5))

#Funcion recursiva Fibonacci
#Imprime la serie Fibonacci hasta el numero n
def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib = fibonacci(n - 1)
        fib.append(fib[-1] + fib[-2])
        return fib
#Ejemplo
print("Serie Fibonacci hasta el 10:", fibonacci(10))