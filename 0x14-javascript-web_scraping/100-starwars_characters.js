#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else if (response.statusCode === 200) {
    const film = JSON.parse(body);
    const characters = film.characters;

    characters.forEach(characterUrl => {
      request(characterUrl, (error, response, body) => {
        if (error) {
          console.error(error);
        } else if (response.statusCode === 200) {
          const character = JSON.parse(body);
          console.log(character.name);
        } else {
          console.error(`Error: ${response.statusCode}`);
        }
      });
    });
  } else {
    console.error(`Error: ${response.statusCode}`);
  }
});
