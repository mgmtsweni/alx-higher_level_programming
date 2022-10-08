#!/usr/bin/node
let list = require('./100-data.js').list;

let newList = list.map((l, i) => l * i);

console.log(list);
console.log(newList);
