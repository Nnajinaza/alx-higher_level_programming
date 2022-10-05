#!/usr/bin/node

const process = require('process');
const myArgs = process.argv;
const nos1 = parseInt(myArgs[2]);

function factorial (a) {
  if (isNaN(a)) {
    return (1);
  } else if (a === 1) {
    return (1);
  } else {
    return (a * factorial(a - 1));
  }
}
console.log(factorial(nos1));
