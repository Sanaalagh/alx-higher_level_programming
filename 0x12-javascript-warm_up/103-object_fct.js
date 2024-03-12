#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12,
  incr: function () {
    this.value++;
    console.log(`{ type: 'object', value: ${this.value}, incr: [Function] }`);
  }
};

console.log(`{ type: 'object', value: ${myObject.value} }`);

myObject.incr();
myObject.incr();
myObject.incr();
