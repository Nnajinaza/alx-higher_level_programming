#!/usr/bin/node

const process = require('process');
const fs = require('fs');
const file1 = process.argv[2];
const file2 = process.argv[3];
const file3 = process.argv[4];

line = '';
line = line.concat(fs.readFileSync(file1));
line = line.concat(fs.readFileSync(file2));
fs.writeFileSync(file3, line);
