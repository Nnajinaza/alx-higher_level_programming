#!/usr/bin/node

const newArr = require('./100-data').list;
const newlist =	newArr.map((x, idx) => x * idx);
console.log(newArr);
console.log(newlist);
