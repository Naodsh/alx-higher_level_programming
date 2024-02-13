#!/usr/bin/node
// Use the process.argv array to access the arguments
const args = process.argv.slice(2); // Slice the first two elements that are not relevant

// Use the first and second elements of the array as the arguments
const arg1 = args[0];
const arg2 = args[1];

// Use the + operator to concatenate the arguments and the " is " string
const sentence = arg1 + ' is ' + arg2;

// Use console.log to print the output
console.log(sentence);
