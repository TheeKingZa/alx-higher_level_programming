#!/usr/bin/node
const list = require('./100-data.js').list;

console.log(list); // Output: [1, 2, 3, 4, 5]

// Using the map function to create a new array
console.log(list.map((item, index) => item * index));
