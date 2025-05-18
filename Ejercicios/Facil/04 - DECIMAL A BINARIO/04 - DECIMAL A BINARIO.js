/*
 * Crea un programa se encargue de transformar un número
 * decimal a binario sin utilizar funciones propias del lenguaje que lo hagan directamente.
 */

const transformar = (decimal) => {
  let binario = "";
  let numeroActual = decimal;

  while (numeroActual !== 0) {
    binario = numeroActual % 2 + binario;
    numeroActual = Math.floor(numeroActual / 2);
  }

  return binario;
};

console.log(transformar(23520));
