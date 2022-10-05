#!/usr/bin/node
const process = require('process');
const myArgs = process.argv.slice(2);
if (myArgs.length < 1) {
  console.log('No argument');
} else if (myArgs.length === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
