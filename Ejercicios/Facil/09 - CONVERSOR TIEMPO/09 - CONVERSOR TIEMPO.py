
#Crea una función que reciba días, horas, minutos y segundos (como enteros)
#y retorne su resultado en milisegundos.

def manualTime(days:int, hr:int, mins:int, segs:int):
    result = 0
    #Tabla de conversion
    # 1s = 1000 ms
    # 1m = 60000 ms
    # 1hr = 3600000 ms
    # 1d = 86400000 ms

    result += segs * 1000
    result += mins * 60000
    result += hr * 3600000
    result += days * 86400000

    print(f"Tu resultado en milisegundos es:{result}")
    return result

manualTime(4,7,20,5)