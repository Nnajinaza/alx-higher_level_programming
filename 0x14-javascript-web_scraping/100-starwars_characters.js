#!/usr/bin/node
const process = require('process');
const request = require('request');

const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;

request.get(url, (err, res, data) => {
  if (!err) {
    const characters = JSON.parse(data).characters;
    characters.forEach((characterUrl) => {
      request.get(characterUrl, (error, response, character) => {
        if (!error) {
          console.log(JSON.parse(character).name);
        }
      });
    });
  }
});
