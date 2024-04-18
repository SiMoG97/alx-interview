#!/usr/bin/node
const request = require('request');

const filmId = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${filmId}`;

request(url, async (err, _, body) => {
  if (err) {
    console.log(err);
    return;
  }

  for (const characterUrl of JSON.parse(body).characters) {
    await new Promise((resolve, reject) => {
      request(characterUrl, (err, _, body) => {
        if (err) {
          reject(err);
        }
        console.log(JSON.parse(body).name);
        resolve();
      });
    });
  }
});
