#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, { json: true }, (err, res, body) => {
  if (err) { return console.log(err); }
  const completed = {};
  body.forEach(task => {
    if (task.completed) {
      completed[task.userId] = (completed[task.userId] || 0) + 1;
    }
  });
  console.log(completed);
});
