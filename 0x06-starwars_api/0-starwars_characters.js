#!/usr/bin/node

const request = require ('request');

request('https://swapi-api.alx-tools.com/api/' + process.argv[2],
function(err, res, body) {
    if (err) throw err;
    const actor = JSON.parse(body).characters;
    order(actor, 0);
});
const order = (actor, x) => {
    if (x === actor.length) return;
    request(actor[x], function (err, res, body) {
      if (err) throw err;
      console.log(JSON.parse(body).name);
      order(actor, x + 1);
    });
  };