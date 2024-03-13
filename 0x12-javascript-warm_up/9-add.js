#!/usr/bin/node
// Define a function with the prototype: function add(a, b)
function add (a, b) {
  // Convert the arguments to integers using the Number function
  const num1 = Number(a);
  const num2 = Number(b);

  // Check if the conversion was successful
  if (isNaN(num1) || isNaN(num2)) {
    // If not, return NaN
    return NaN;
  } else {
    // If yes, return the sum of the two integers
    return num1 + num2;
  }
}

// Get the first and second arguments from the command line
const arg1 = process.argv[2];
const arg2 = process.argv[3];

// Call the add function with the arguments and store the result
const result = add(arg1, arg2);

// Print the result using console.log
console.log(result);
