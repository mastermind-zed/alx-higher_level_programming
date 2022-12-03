#!/usr/bin/node
const mySq = Math.floor(Number(process.argv[2]));
let rows = 'X';

if (isNaN(mySq)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < mySq - 1; i++) {
    rows += 'X';
  }
  for (let j = 0; j < mySq; j++) {
    console.log(rows);
  }
}
