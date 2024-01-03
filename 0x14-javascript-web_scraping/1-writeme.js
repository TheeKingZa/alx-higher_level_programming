#!/usr/bin/node

// Import the 'fs' module for file system operations
const fs = require('fs');

// Use fs.writeFile to asynchronously write data to a file
// The data to be written is specified by command line arguments
// The first argument (process.argv[2]) is the file path
// The second argument (process.argv[3]) is the content to be written
// The third argument is a callback function executed once the write operation is complete or an error occurs
fs.writeFile(process.argv[2], process.argv[3], error => {
  // The callback function receives one parameter: error

  // Check if there is an error during the write operation
  if (error) {
    // If there is an error, log the error to the console
    console.log(error);
  }
});

// Note: process.argv is an array that contains the command line arguments
// process.argv[0] is the path to the Node.js executable
// process.argv[1] is the path to the script being run
// process.argv[2] is the first command line argument, which is expected to be the file path
// process.argv[3] is the second command line argument, which is expected to be the content to be written to the file
