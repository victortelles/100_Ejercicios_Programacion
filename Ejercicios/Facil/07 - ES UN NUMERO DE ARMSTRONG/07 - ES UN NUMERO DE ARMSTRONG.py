#Escribe una función que calcule si un número dado es un número de Armstrong
#(o también llamado narcisista).
#Si no conoces qué es un número de Armstrong, debes buscar información
#al respecto.

# pow(base, exponente) || ** = ^  potencia

def armStrong(n):
    #conversion a string
    longitud = str(n)
    print("Conversion de str")
    print(f"{longitud}")
    #Contar longitud caracteres
    exponente = len(longitud)
    print("Longitud")
    print(f"{exponente}")

    # n^exponente
    resultado = 0
    for item in longitud:
        base = int(item)
        # pow(base, exponente)
        op = pow(base, exponente)

        #suma (n^e + n^e....)
        resultado += op
    print(resultado)

    if(resultado == n):
        print('Si es un numero Armstrong')
        return True
    else:
        print("No es un fucking numero Armstrong")
        return False


#Test
armStrong(7515)
