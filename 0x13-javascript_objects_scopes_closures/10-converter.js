#!/usr/bin/node
exports.converter = function (base) {
  function currentBase (number) {
    return number.toString(base);
  }

  return currentBase;
};
