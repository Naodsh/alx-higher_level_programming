#!/usr/bin/node
// Define a function that takes an integer as an argument
function factorial (n) {
  const num = Number(n);
  if (isNaN(num) || num === 0) {
    return 1;
  }

  if (num < 0) {
    return undefined;
  }
  return num * factorial(num - 1);
}

const arg = process.argv[2];
const result = factorial(arg);
console.log(result);
