#!/usr/bin/node

const process = require('process');
const myArgs = process.argv;
const nos = parseInt(myArgs[2]);
if (isNaN(nos)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + nos);
}
