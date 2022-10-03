#!/usr/bin/node

const a = parseInt(process.argv[2]);
const b = parseInt(process.argv[3]);

function add(l, i) {
    if (isNaN(i) || isNaN(l)){
        return NaN;
    } else {
        return (i + l);
    }
}

console.log(add(a,b));
