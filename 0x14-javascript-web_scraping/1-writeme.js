#!/usr/bin/node
const fs = require('fs');
const file1 = process.argv[2];
const string1 = process.argv[3];
fs.writeFile(file1, string1, 'utf8', (err) => {
  if (err) {
    console.log(err);
  }
});
