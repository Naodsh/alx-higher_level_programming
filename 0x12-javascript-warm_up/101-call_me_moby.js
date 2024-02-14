#!/usr/bin/node
// Executes a function x times
function callMeMoby (x, theFunction) {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
}

module.exports.callMeMoby = callMeMoby;
