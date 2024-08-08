#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

function fetchCharacterNames(characterUrls, index) {
  if (index >= characterUrls.length) {
    return;
  }

  request(characterUrls[index], (error, response, body) => {
    if (error) {
      console.error('Error fetching character data:', error);
    } else {
      const characterData = JSON.parse(body);
      console.log(characterData.name);
      fetchCharacterNames(characterUrls, index + 1);
    }
  });
}

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error fetching movie data:', error);
    return;
  }

  const movieData = JSON.parse(body);
  const characterUrls = movieData.characters;

  fetchCharacterNames(characterUrls, 0);
});
