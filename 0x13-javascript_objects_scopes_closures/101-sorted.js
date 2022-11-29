#!/usr/bin/node
const dict = require('./101-data').dict;
const currentDict = {};

for (const key in dict) {
  if (currentDict[dict[key]] === undefined) {
    currentDict[dict[key]] = [key];
  } else {
    currentDict[dict[key]].push(key);
  }
}
console.log(currentDict);
