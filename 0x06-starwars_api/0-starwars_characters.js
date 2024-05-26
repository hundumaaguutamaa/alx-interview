#!/usr/bin/node


const request = require('request');

const movieId = process.argv[2];
const movieEndpoint = 'https://swapi-api.alx-tools.com/api/films/' + movieId;

// Recursive function to fetch and print character names.
function sendRequest(charactersl, index) {
  if (charactersl.length === index) {
    return;
  }

  // Make HTTP request, handle error, parse, and print character name.
  request(charactersl[index], (error, response, body) => {
    if (error) {
      console.log(error);
    } else {
      console.log(JSON.parse(body).name);
      index += 1;
      sendRequest(charactersl, index);
    }
  });
}

// Initial request to fetch movie details.
request(movieEndpoint, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const charactersl = JSON.parse(body).characters;
    sendRequest(charactersl, 0);
  }
});
