#!/usr/bin/node
const x = parseInt(process.argv[2]);
function factorial (x) {
  if (isNaN(x) || x === 0 || x === 1) {
    return 1;
  } else {
    return x * factorial(x - 1);
  }
}
const y = factorial(x);
console.log(y);
