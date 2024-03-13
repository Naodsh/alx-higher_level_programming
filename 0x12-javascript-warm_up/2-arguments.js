#!/usr/bin/node
const args = process.argv.slice(2);

const numArgs = args.length;

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
