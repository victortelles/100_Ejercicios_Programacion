/*
 * Crea una función que reciba un String de cualquier tipo y se encargue de
 * poner en mayúscula la primera letra de cada palabra.
 * - No se pueden utilizar operaciones del lenguaje que
 *   lo resuelvan directamente.
 */

// const letras = {
//   a: "A",
//   b: "B",
//   c: "C",
//   d: "D",
//   e: "E",
//   f: "F",
//   g: "G",
//   h: "H",
//   i: "I",
//   j: "J",
//   k: "K",
//   l: "L",
//   m: "M",
//   n: "N",
//   o: "O",
//   p: "P",
//   q: "Q",
//   r: "R",
//   s: "S",
//   t: "T",
//   u: "U",
//   v: "V",
//   w: "W",
//   x: "X",
//   y: "Y",
//   z: "Z",
// };

// const firstLetterMayus = (str) => {
//   const palabras = str.split(" ");
//   let mayus = "";

//   for (let i = 0; i < palabras.length; i++) {
//     mayus += palabras[i].replace(palabras[i][0], letras[palabras[i][0]]) + " ";

//     palabras[i][0];
//   }

//   return mayus.trim();
// };

// console.log(firstLetterMayus("hola mundo"));



const minusculas = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "y", "z"]
const mayusculas = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "Y", "Z"]

const firstLetterMayus = (str) => {
  const palabras = str.split(" ");
  let mayus = "";

  for (let i = 0; i < palabras.length; i++) {
    let index = minusculas.indexOf(palabras[i][0])
    mayus += palabras[i].replace(palabras[i][0], mayusculas[index]) + " ";
    palabras[i][0];
  }

  return mayus.trim();
};

console.log(firstLetterMayus("hola mundo test"));