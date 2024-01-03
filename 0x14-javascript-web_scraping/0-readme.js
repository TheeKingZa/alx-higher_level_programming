#!/usr/bin/node

// Import the 'fs' module for file system operations
const fs = require('fs');

// Use fs.readFile to asynchronously read the file specified in the command line arguments
// 'utf8' specifies the encoding of the file content to be read
// The callback function is executed once the file is read or an error occurs
fs.readFile(process.argv[2], 'utf8', function (error, content) {
  // The callback function receives two parameters: error and content

  // If there is an error during file reading, print the error
  // Otherwise, print the content of the file
  console.log(error || content);
});

// Note: process.argv is an array that contains the command line arguments
// process.argv[0] is the path to the Node.js executable
// process.argv[1] is the path to the script being run
// process.argv[2] is the first command line argument, which is expected to be the file path in this script
