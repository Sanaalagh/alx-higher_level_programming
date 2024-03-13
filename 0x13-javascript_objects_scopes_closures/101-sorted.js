#!/usr/bin/node
const { dict } = require('./101-data.js');
const newDict = Object.entries(dict).reduce((acc, [key, value]) => {
  if (!acc[value]) {
    acc[value] = [];
  }
  acc[value].push(key);
  return acc;
}, {});

console.log(newDict);
