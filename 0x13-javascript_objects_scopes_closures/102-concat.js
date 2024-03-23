#!/usr/bin/node
const fs = require('fs');

const sourceFile1 = process.argv[2];
const sourceFile2 = process.argv[3];
const destinationFile = process.argv[4];

const fileContent1 = fs.readFileSync(sourceFile1, 'utf8');
const fileContent2 = fs.readFileSync(sourceFile2, 'utf8');

const concatenatedContent = fileContent1 + '\n' + fileContent2;

fs.writeFileSync(destinationFile, concatenatedContent);

