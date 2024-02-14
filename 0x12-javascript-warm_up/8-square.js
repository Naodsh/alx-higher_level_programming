#!/usr/bin/node
// Get the first argument from the command line
const size = process.argv[2];

// Convert the argument to an integer using the Number function
const num = Number(size);

// Check if the conversion was successful and the number is positive
if (isNaN(num) || num <= 0) {
  // If not, print "Missing size"
  console.log('Missing size');
} else {
  // If yes, use a for loop to print num rows
  for (let i = 0; i < num; i++) {
    // Use the repeat method to create a string of num X characters
    const row = 'X'.repeat(num);
    // Print the row
    console.log(row);
  }
}
