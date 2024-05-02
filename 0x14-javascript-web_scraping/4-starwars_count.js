#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, { json: true }, (err, res, body) => {
  if (err) { return console.log(err); }
  const films = body.results.filter(film =>
    film.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')
  );
  console.log(films.length);
});
