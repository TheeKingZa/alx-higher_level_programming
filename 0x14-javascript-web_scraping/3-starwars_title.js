#!/usr/bin/env node

// Import the 'request' module for making HTTP requests
const request = require('request');

// Retrieve the episode number from the command line arguments
const episodeNum = process.argv[2];

// Define the API URL for fetching Star Wars film information
const API_URL = 'https://swapi-api.hbtn.io/api/films/';

// Make a GET request to the Star Wars API with the specified episode number
request(API_URL + episodeNum, function (err, response, body) {
  // The callback function receives three parameters: err, response, and body

  // Check if there is an error during the request
  if (err) {
    // If there is an error, log the error to the console
    console.log(err);
  } else if (response.statusCode === 200) {
    // If the response status code is 200 (OK), parse the JSON response body
    const responseJSON = JSON.parse(body);

    // Print the title of the Star Wars film
    console.log(responseJSON.title);
  } else {
    // If the response status code is not 200, log an error message with the status code
    console.log('Error code: ' + response.statusCode);
  }
});
