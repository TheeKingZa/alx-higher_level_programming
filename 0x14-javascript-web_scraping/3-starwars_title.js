#!/usr/bin/node

// Import the 'request' module for making HTTP requests
const request = require('request');

// Retrieve the movie ID from the command line arguments
const movieId = process.argv[2];

// Construct the API URL using the provided movie ID
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Make an HTTP request to the Star Wars API
request(apiUrl, (error, response, body) => {
  // Handle any errors that may occur during the request
  if (error) {
    console.error(error);
    // Exit the script with a non-zero status code to indicate an error
    process.exit(1);
  }

  // Check if the response status code is 200 (OK)
  if (response.statusCode === 200) {
    // Parse the JSON response body into an object
    const movie = JSON.parse(body);
    // Display the episode number and title of the movie
    console.log(`Episode ${movie.episode_id}: ${movie.title}`);
  } else {
    // Display an error message if the response status code is not 200
    console.error(`Error: ${response.statusCode}`);
    // Exit the script with a non-zero status code to indicate an error
    process.exit(1);
  }
});
