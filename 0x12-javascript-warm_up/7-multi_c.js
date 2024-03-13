#!/usr/bin/node
const arg = process.argv[2];

let x = Number(arg);

if (isNaN(x)) {
  console.log('Missing number of occurrences');
} else {
  while (x > 0) {
    console.log('C is fun');
    x--;
  }
}
