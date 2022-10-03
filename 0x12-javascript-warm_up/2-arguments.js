#!/usr/bin/node
const myArgs = process.argv.slice(2);
if (myArgs < 1) {
	console.log("No argument");
} else if (myArgs === 2) {
	console.log("Argument found");
} else {
	console.log("Arguments found");
};
