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

    // Function to fetch and print character names in order
    const fetchCharacter = (index) => {
      if (index >= characters.length) return;

      request(characters[index], (error, response, body) => {
        if (error) {
          console.error(error);
        } else if (response.statusCode === 200) {
          const character = JSON.parse(body);
          console.log(character.name);
          fetchCharacter(index + 1); // Fetch the next character
        } else {
          console.error(`Error: ${response.statusCode}`);
        }
      });
    };

    // Start fetching characters from the first one
    fetchCharacter(0);
  } else {
    console.error(`Error: ${response.statusCode}`);
  }
});
