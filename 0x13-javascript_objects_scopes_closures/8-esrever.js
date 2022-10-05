#!/usr/bin/node

exports.esrever = function (list) {
  for (let i = 0; i < list.length - 1; i++) {
    list.splice(i, 0, list.pop());
  }
  return (list);
};
