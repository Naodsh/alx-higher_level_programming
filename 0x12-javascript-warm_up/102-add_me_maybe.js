#!/usr/bin/node
// Increments and calls a function
function addMeMaybe (number, theFunction) {
  number++;
  theFunction(number);
}

module.exports.addMeMaybe = addMeMaybe;
