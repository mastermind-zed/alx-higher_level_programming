#!/usr/bin/node
function * generator () {
  let idx = 0;
  while (true) {
    yield idx++;
  }
}

const gen = generator();

exports.logMe = function (item) {
  console.log(gen.next().value + ': ' + item);
};

