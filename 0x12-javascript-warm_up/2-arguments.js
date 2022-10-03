#!/usr/bin/node

const NumArg = process.argv.length;

if (NumArg === 2) {
  console.log('No argument');
} else if (NumArg === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}