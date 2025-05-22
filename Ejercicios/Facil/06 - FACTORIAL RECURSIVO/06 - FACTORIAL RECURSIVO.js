/*
 * Escribe una función que calcule y retorne el factorial de un número dado
 * de forma recursiva.
 */

let res;
const factorial = (num) => {
  if (num === 0) {
    return 1;
  } else {
    res = num * factorial(num - 1);
  
    return res;
  }
  
};

console.log(factorial(9));
