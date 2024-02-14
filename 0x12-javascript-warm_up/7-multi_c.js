#!/usr/bin/node
// Get the first argument from the command line
const arg = process.argv[2];

// Convert the argument to an integer using the Number function
let x = Number(arg);

// Check if the conversion was successful and the number is positive
if (isNaN(x) || x <= 0) {
  // If not, print "Missing number of occurrences"
  console.log('Missing number of occurrences');
} else {
  // If yes, use a while loop to print "C is fun" x times
  while (x > 0) {
    console.log('C is fun');
    x--;
  }
}
