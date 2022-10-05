#!/usr/bin/node

exports.converter = function (base) {
  function convert (dec) {
    return dec.toString(base);
  } return convert;
};
