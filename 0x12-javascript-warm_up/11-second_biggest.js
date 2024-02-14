#!/usr/bin/node
// Define a function that takes an array of arguments as a parameter
function secondBiggest (args) {
  // Initialize two variables to store the biggest and second biggest integers
  let biggest = -Infinity;
  let second = -Infinity;

  // Loop through the array of arguments
  for (const arg of args) {
    // Convert the argument to a number using the Number function
    const num = Number(arg);

    // Check if the number is bigger than the biggest
    if (num > biggest) {
      // If yes, update the second and the biggest
      second = biggest;
      biggest = num;
    } else if (num > second && num < biggest) {
      // If the number is in between the second and the biggest, update the second
      second = num;
    }
  }

  // Return the second biggest integer, or 0 if not found
  return second === -Infinity ? 0 : second;
}

// Get the array of arguments from the command line, excluding the first two elements
const args = process.argv.slice(2);

// Call the secondBiggest function with the arguments and store the result
const result = secondBiggest(args);

// Print the result using console.log
console.log(result);
