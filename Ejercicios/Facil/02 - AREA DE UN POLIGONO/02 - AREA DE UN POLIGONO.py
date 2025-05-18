# Crea una única función (importante que sólo sea una) que sea capaz
# de calcular y retornar el área de un polígono.
#- La función recibirá por parámetro sólo UN polígono a la vez.
#- Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
#- Imprime el cálculo del área de un polígono de cada tipo.

def area(poligono, base, altura):
    if (poligono == "triangulo"):
        area = (base * altura) / 2
        print(f"El area del triangulo es: {area}")
        return area

    elif (poligono == "cuadrado"):
        area = base * base
        print(f"El area del cuadrado es: {area}")
        return area

    elif (poligono == "rectangulo"):
        area = base * altura
        print(f"El area del rectangulo es: {area}")
        return area
    else:
        print("No hay, no existe")
    return poligono

#Test
area("triangulo", 3, 5)
area("rectangulo", 4, 6)
area("cuadrado", 4, 4)
area("asdasda",0  ,0)