#!/usr/bin/node

const firstArg = parseInt(process.argv[2]);

if (isNaN(firstArg)) {
  console.log('Missing number of occurrences');
} else {
    i = 0;
    while (i < firstArg) {
        console.log('C is fun');
        i++;
    }
}
