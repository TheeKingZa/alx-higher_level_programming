#!/usr/bin/node
// Import the 'request' module for making HTTP requests
const request = require('request');

// Use request.get to make a GET request to the URL specified by the command line argument
// The response is handled using the 'response' event
request.get(process.argv[2]).on('response', function (response) {
  // The callback function receives the 'response' object

  // Print the status code of the HTTP response
  console.log('code: ${response.statusCode}');
});
