#Crea un programa se encargue de transformar un número
#decimal a binario sin utilizar funciones propias del lenguaje que lo hagan directamente.

def transformar (decimal):
    """Transformar num entero a binario"""
    # Obtener el valor por parte del usuario
    print(f"Decimal del usuario: {decimal}")
    # Declarar variables y referenciarlos
    binario = ""
    num_act = decimal

    #Division secuencial
    while num_act != 0:
        # Tomar valor si hay residuo
        residuo = num_act % 2
        # conversion de float -> int y operacion division
        num_act = int(num_act / 2)
        # binario obtiene el valor residuo y el valor anterior
        binario = str(residuo) + binario
        print(num_act)
    print(f"El numeor binario es {binario}")

#test
transformar(23519)
transformar(10)
transformar(9)
transformar(5050)
transformar(2001)