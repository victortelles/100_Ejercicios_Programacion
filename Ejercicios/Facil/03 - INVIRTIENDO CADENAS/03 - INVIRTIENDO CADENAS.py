#
#Crea un programa que invierta el orden de una cadena de texto
#sin usar funciones propias del lenguaje que lo hagan de forma automática.
# - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
#

# Opcion 1
#texto = "Hola Mundo"[::-1]
#print(texto)
#
#character = ""
#for character in texto[::-1]:
#    print(character)
#    inversed_text
#    print(inversed_text)


# Opcion 2
texto = "Hola Mundo"
i = len(texto) -1
inverted = ""

while i >= 0:
    #print(texto[i])
    inverted += texto[i]
    i -= 1
print(inverted)