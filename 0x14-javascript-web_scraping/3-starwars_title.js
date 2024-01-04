#!/usr/bin/node

// This script retrieves information about a Star Wars movie based on its episode ID.
// It uses the 'axios' library to make an HTTP request to the Star Wars API.
// The API response is then parsed to extract and display the episode number and title of the movie.

// Import the 'axios' library for making HTTP requests
const axios = require('axios');

// Retrieve the movie ID from the command line arguments
const movieId = process.argv[2];

// Construct the API URL using the provided movie ID
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Make an HTTP GET request to the Star Wars API using 'axios'
axios.get(apiUrl)
  .then(response => {
    // Extract the movie data from the response
    const movie = response.data;
    // Display the episode number and title of the movie
    console.log(`Episode ${movie.episode_id}: ${movie.title}`);
  })
  .catch(error => {
    // Handle errors during the HTTP request
    console.error(error.message);
    // Exit the script with a non-zero status code to indicate an error
    process.exit(1);
  });
