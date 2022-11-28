#!/usr/bin/node
if (process.argv.length === 2) {
  console.log('No argument');
}
if (process.argv.length === 3) {
  console.log('Argument found');
}
if (process.argv.length > 3) {
  console.log('Arguments found');
}
