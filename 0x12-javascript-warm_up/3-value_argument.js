#!/usr/bin/node
if (process.argv[2] == null) {
  console.log('No argument');
} else {
  const x = process.argv[2];
  console.log(x);
}
