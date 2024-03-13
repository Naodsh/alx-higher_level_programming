#!/usr/bin/node
// Get the first argument from the command line
const arg = process.argv[2];

// Convert the argument to an integer using the parseInt function
const num = parseInt(arg, 10);

// Check if the conversion was successful
if (isNaN(num)) {
  // If not, print "Not a number"
  console.log('Not a number');
} else {
  // If yes, print "My number: " followed by the integer
  console.log('My number: ' + num);
}
