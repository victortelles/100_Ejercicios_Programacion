/*
 * Crea un programa que invierta el orden de una cadena de texto
 * sin usar funciones propias del lenguaje que lo hagan de forma automática.
 * - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
 */

const inversor = (cadena) => {
  let cadenaInversa = "";
  for (let i = cadena.length - 1; i >= 0; i--) {
    cadenaInversa += cadena[i];
  }
  return cadenaInversa;
};

console.log(inversor("Hola prros"))
