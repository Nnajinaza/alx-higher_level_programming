#!/usr/bin/node

const process = require('process');
const myArgs = process.argv;
const nos = parseInt(myArgs[2]);

if (isNaN(nos)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < nos; i++) {
    console.log('C is fun');
  }
}
