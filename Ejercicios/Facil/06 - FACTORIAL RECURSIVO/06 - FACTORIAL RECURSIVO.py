# Escribe una función que calcule y retorne el factorial
# de un número dado de forma recursiva.

# (n-1)
#def multiplicacion(n):
#
#    for item in range(1, n):
#        item = 1
#        n -= item
#        result = n
#        print(f"Numero: {result}")
#
#    return result
#
# n(n-1)!
def factorial(n):
    if(n==0):
        return 1
    else:
        result = n * factorial(n-1)
        print(result)
        return result

#    for item in range(n):
#        n =- item
#        result = n * multiplicacion(n)
#        print(result)
#    return result

# Solicitar valor al usuario
n = int(input("Ingresa un numero, para factorizar:  "))
print(f"El factorial de: {n} es: {factorial(n)}")
#factorial(5)