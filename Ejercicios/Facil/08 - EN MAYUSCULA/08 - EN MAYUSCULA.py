
#Crea una función que reciba un String de cualquier tipo y se encargue de
#poner en mayúscula la primera letra de cada palabra.
#- No se pueden utilizar operaciones del lenguaje que
#  lo resuelvan directamente.
minus = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
mayus = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def mayusFirst(text: str):
    print(f"El Texto ingresado es:\n{text}")
    #Quitar los espacios
    text = text.split()
    #print(text)

    i = 0
    resultado = ""
    
    for item in text:
        #palabra
        #print(item)
        # obtengo el primer elemento de la palabra
        #print(text[i][0])

        # Busco el indice del arreglo
        indice_minus = minus.index(text[i][0])

        # Remplaza el primer elemento del indice por la mayuscula y lo junta
        resultado += text[i].replace(text[i][0], mayus[indice_minus], 1) + " "
        #print(resultado.strip())

        #Paso al siguiente palabra
        i += 1
        #print(indice_minus)

    print(f"El Texto queda:\n{resultado.strip()}")
    #print(first_mayus)
    return

#Testing
mayusFirst('hola mundo test aaaabvcsa')
mayusFirst('espartan nunca muere')
mayusFirst('discord skype spotify')