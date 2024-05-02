#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url, { json: true }, (err, res, body) => {
  if (err) { return console.log(err); }
  const charactersUrls = body.characters;
  const charactersPromises = charactersUrls.map(characterUrl => {
    return new Promise((resolve, reject) => {
      request(characterUrl, { json: true }, (err, res, body) => {
        if (err) { reject(err); }
        resolve(body.name);
      });
    });
  });
  Promise.all(charactersPromises)
    .then(characters => {
      characters.forEach(character => console.log(character));
    })
    .catch(err => console.error(err));
});
