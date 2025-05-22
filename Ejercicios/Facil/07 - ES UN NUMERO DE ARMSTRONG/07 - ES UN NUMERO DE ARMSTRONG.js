/*
 * Escribe una función que calcule si un número dado es un número de Armstrong
 * (o también llamado narcisista).
 * Si no conoces qué es un número de Armstrong, debes buscar información
 * al respecto.
 */

const armstrong = (num) => {
console.log(num.length)
  const numeros = num.toString().split("");
  let res = 0;
  for (let i = 0; i < numeros.length; i++) {
    res += Math.pow(parseInt(numeros[i]), numeros.length);
  }

  return res === num ? true : false;
};

console.log(armstrong(407));
