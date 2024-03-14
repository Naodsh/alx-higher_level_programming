#!/usr/bin/node
// Define a function that takes an array of arguments as a parameter
// and Return the second biggest integer

function secondBiggest (args) {
  let biggest = -Infinity;
  let second = -Infinity;

  for (const arg of args) {
    const num = Number(arg);
    if (num > biggest) {
      second = biggest;
      biggest = num;
    } else if (num > second && num < biggest) {
      second = num;
    }
  }

  return second === -Infinity ? 0 : second;
}

const args = process.argv.slice(2);
const result = secondBiggest(args);
console.log(result);
