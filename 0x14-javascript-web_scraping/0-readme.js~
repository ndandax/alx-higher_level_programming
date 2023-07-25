#!/usr/bin/node

file1 = process.argv[2];
const fs = require('fs');
fs.readFile(file1, 'utf8', (err, data) => {
  if (err) {
    console.error(err);
  } else {
    console.log(data);
  }
});
