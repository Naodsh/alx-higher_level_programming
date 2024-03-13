#!/usr/bin/node
// Use the process.argv array to access the arguments
const args = process.argv.slice(2); // Slice the first two elements that are not relevant

// Use the first element of the array as the first argument
const firstArg = args[0];

// Check if the first argument is undefined or not
if (firstArg === undefined) {
  console.log('No argument');
} else {
  console.log(firstArg);
}
