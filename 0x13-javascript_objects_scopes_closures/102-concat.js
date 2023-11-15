#!/usr/bin/node
// The above line is a shebang indicating that the script should be run using the specified interpreter, in this case, 'node'.

const fs = require('fs');

// Read the content of the first file specified by the first command-line argument
const fArg = fs.readFileSync(process.argv[2]).toString();

// Read the content of the second file specified by the second command-line argument
const sArg = fs.readFileSync(process.argv[3]).toString();

// Concatenate the contents of the two files
// Write the concatenated content to a new file specified by the third command-line argument
fs.writeFileSync(process.argv[4], fArg + sArg);

