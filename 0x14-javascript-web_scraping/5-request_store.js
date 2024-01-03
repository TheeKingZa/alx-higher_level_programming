#!/usr/bin/node

// Import the 'fs' module for file system operations
const fs = require('fs');

// Import the 'request' module for making HTTP requests
const request = require('request');

// Make a GET request to the URL specified by the first command line argument
// Pipe the response stream directly to a writable stream (file) specified by the second command line argument
request(process.argv[2]).pipe(fs.createWriteStream(process.argv[3]));
