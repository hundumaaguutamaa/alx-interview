#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const movieURL = 'https://swapi.dev/api/films/' + movieId;

function fetchCharacters(characterURLs) {
  characterURLs.forEach(characterURL => {
    request(characterURL, (error, response, body) => {
      if (error) {
        console.error('Error:', error);
      } else if (response.statusCode !== 200) {
        console.error('Status Code:', response.statusCode);
      } else {
        const character = JSON.parse(body);
        console.log(character.name);
      }
    });
  });
}

request(movieURL, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else if (response.statusCode !== 200) {
    console.error('Status Code:', response.statusCode);
  } else {
    const film = JSON.parse(body);
    const characterURLs = film.characters;

    fetchCharacters(characterURLs);
  }
});
