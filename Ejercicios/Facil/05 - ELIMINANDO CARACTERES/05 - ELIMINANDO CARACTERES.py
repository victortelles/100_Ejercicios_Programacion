
#Crea una función que reciba dos cadenas como parámetro ✔️(str1, str2)e imprima otras dos cadenas como salida (out1, out2).
#- ✔️out1 contendrá todos los caracteres presentes en la str1 pero NO estén presentes en str2.
#- ✔️out2 contendrá todos los caracteres presentes en la str2 pero NO estén presentes en str1.

def deleteCaracteres(str1: str, str2: str):

    out1= str1.lower()
    out2= str2.lower()

    print(len(str1)) #12

    for letra in str1:
        out2 = out2.replace(letra.lower(), "")
    print(out2)

    for letra in str2:
        out1 = out1.replace(letra.lower(), "")
    print(out1)

deleteCaracteres("Python Chafa", "QlorpAnt Cafe")