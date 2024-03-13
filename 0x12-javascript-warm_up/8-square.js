#!/usr/bin/node
const size = process.argv[2];

const num = Number(size);

if (isNaN(num) || num <= 0) {
  console.log('Missing size');
} else {
  for (let i = 0; i < num; i++) {
    const row = 'X'.repeat(num);
    console.log(row);
  }
}
