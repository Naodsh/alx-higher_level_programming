#!/usr/bin/node
const { dict } = require('./101-data');

const sortedDict = {};

Object.keys(dict).forEach(key => {
  const occurrences = dict[key];
  if (!sortedDict[occurrences]) {
    sortedDict[occurrences] = [];
  }
  sortedDict[occurrences].push(key);
});

console.log(sortedDict);
