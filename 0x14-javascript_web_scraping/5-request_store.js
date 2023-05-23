#!/usr/bin/node
const fs = require('fs');
const request = require('request');
request(process.argv[2], 'utf-8', function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    fs.writeFile(process.argv[3], body, function (err) {
      if (err) {
        console.log(err);
      }
    });
  }
});
