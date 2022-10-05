#!/usr/bin/node

let nos = 0;
exports.logMe = function (item) {
  console.log(`${nos}: ${item}`);
  nos++;
};
