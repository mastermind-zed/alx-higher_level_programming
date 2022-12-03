#!/usr/bin/node
if (process.argv.length < 4) {
  console.log('0');
} else {
  const args = [];

  for (let x = 2; x < process.argv.length; x++) {
    args[x - 2] = process.argv[x];
  }
  args.sort(function (a, b) { return b - a; });
  console.log(args[1]);
}
