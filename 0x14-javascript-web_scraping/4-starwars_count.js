#!/usr/bin/node

// Import the 'request' module for making HTTP requests
const request = require('request');

// Make a GET request to the specified URL provided as the command line argument
request(process.argv[2], function (error, response, body) {
  // The callback function receives three parameters: error, response, and body

  // Check if there is no error during the request
  if (!error) {
    // Parse the JSON response body and extract the 'results' property
    const results = JSON.parse(body).results;

    // Count the number of movies where the character with ID 18 ('Wedge Antilles') is present
    console.log(results.reduce((count, movie) => {
      return movie.characters.find((character) => character.endsWith('/18/'))
        ? count + 1
        : count;
    }, 0));
  }
});
