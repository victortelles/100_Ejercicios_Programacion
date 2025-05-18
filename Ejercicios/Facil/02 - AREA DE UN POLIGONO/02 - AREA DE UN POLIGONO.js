/*
 * Crea una única función (importante que sólo sea una) que sea capaz
 * de calcular y retornar el área de un polígono.
 * - La función recibirá por parámetro sólo UN polígono a la vez.
 * - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
 * - Imprime el cálculo del área de un polígono de cada tipo.
 */

const area = (poligono, base, altura) => {
  if (poligono === "Triángulo") {
    return (base * altura) / 2;
  }
  if (poligono === "Cuadrado" || poligono === "Rectángulo") {
    return base * altura;
  }
  return "El polígono recibido es incorrecto";
};

console.log(area("Triángulo", 5, 10));
console.log(area("Cuadrado", 7, 7));
console.log(area("Triángulo", 9, 3));
