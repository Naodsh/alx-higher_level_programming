#!/usr/bin/node
// Define a function that takes an integer as an argument
function factorial (n) {
  // Convert the argument to a number using the Number function
  const num = Number(n);

  // Check if the number is NaN or 0
  if (isNaN(num) || num === 0) {
    // If yes, return 1
    return 1;
  }

  // Check if the number is negative
  if (num < 0) {
    // If yes, return undefined
    return undefined;
  }

  // Otherwise, return the number multiplied by the factorial of the number minus one
  return num * factorial(num - 1);
}

// Get the first argument from the command line
const arg = process.argv[2];

// Call the factorial function with the argument and store the result
const result = factorial(arg);

// Print the result using console.log
console.log(result);
