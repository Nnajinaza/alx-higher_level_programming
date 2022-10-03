#!/usr/bin/node
const myArgs = process.argv.slice(2);
if (myArgs < 1) {
		console.log("No argument");
} else {
		console.log("Arguments found");
};
