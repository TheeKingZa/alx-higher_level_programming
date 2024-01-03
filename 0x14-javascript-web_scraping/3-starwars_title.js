#!/usr/bin/node

// Import the 'request' module for making HTTP requests
const request = require('request');

/**
 * Prints the title of a Star Wars movie based on the given movie ID.
 * @param {number} movieId - The ID of the Star Wars movie.
 */
function getStarWarsTitle(movieId) {
    // Construct the URL using the provided endpoint and movie ID
    const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

    // Use the request module to make a GET request to the Star Wars API
    request.get(apiUrl, (error, response, body) => {
        // The callback function receives three parameters: error, response, and body

        if (error) {
            // If there is an error during the request, print the error
            console.error(error);
        } else {
            // Parse the JSON response body
            const movieData = JSON.parse(body);

            // Print the title of the Star Wars movie
            console.log(movieData.title);
        }
    });
}

// Check if the script is called with the correct number of arguments
if (process.argv.length !== 3) {
    // Print an error message if the correct number of arguments is not provided
    console.error('Usage: ./3-starwars_title.js <movie-id>');
} else {
    // Extract the movie ID from the command line arguments
    const movieId = process.argv[2];

    // Call the function to get and print the title of the Star Wars movie
    getStarWarsTitle(movieId);
}
