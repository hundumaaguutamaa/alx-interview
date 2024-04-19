#!/usr/bin/node

const request = require('request');

const movieIdentifier = process.argv[2];
const movieURL = 'https://swapi-api.alx-tools.com/api/films/' + movieIdentifier;

request(movieURL, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const charactersURLs = JSON.parse(body).characters;

    charactersURLs.forEach(characterURL => {
      request(characterURL, (error, response, body) => {
        if (error) {
          console.log(error);
        } else {
          console.log(JSON.parse(body).name);
          console.log(character.name);
        }
      });
    });
  }
});
