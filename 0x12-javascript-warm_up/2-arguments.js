#!/usr/bin/node
// Use the process.argv array to access the arguments
const args = process.argv.slice(2); // Slice the first two elements that are not relevant

// Use the length property of the array to get the number of arguments
const numArgs = args.length;

// Use a switch statement to print different messages based on the number of arguments
switch (numArgs) {
  case 0:
    console.log('No argument');
    break;
  case 1:
    console.log('Argument found');
    break;
  default:
    console.log('Arguments found');
}
