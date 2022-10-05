#!/usr/bin/node

const process = require('process');
const myArgs = process.argv;
const nos1 = parseInt(myArgs[2]);
const nos2 = parseInt(myArgs[3]);

function add (a, b) {
  return (a + b);
}
console.log(add(nos1, nos2));
