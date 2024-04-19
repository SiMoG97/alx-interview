#!/usr/bin/node
const request = require('request');

if (process.argv.length > 2) {
  const filmId = process.argv[2];
  const url = `https://swapi-api.hbtn.io/api/films/${filmId}`;

  request(url, (err, _, body) => {
    if (err) {
      console.log(err);
    }
    const charactersURL = JSON.parse(body).characters;

    const charactersName = charactersURL.map(
      (url) =>
        new Promise((resolve, reject) => {
          request(url, (error, __, charactResBody) => {
            if (error) {
              reject(error);
            }
            resolve(JSON.parse(charactResBody).name);
          });
        })
    );

    //
    Promise.all(charactersName)
      .then((names) => console.log(names.join('\n')))
      .catch((e) => console.log(e));
  });
}
