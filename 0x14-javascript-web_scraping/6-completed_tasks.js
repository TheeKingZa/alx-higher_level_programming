#!/usr/bin/node

// Import the 'request' module for making HTTP requests
const request = require('request');

// Retrieve the URL from the command line arguments
const url = process.argv[2];

// Make a GET request to the specified URL
request(url, function (err, response, body) {
  // The callback function receives three parameters: err, response, and body

  // Check if there is an error during the request
  if (err) {
    // If there is an error, log the error to the console
    console.log(err);
  } else if (response.statusCode === 200) {
    // If the response status code is 200 (OK), parse the JSON response body
    const completed = {};
    const tasks = JSON.parse(body);

    // Iterate through the tasks to count completed tasks by user id
    for (const i in tasks) {
      const task = tasks[i];

      // Check if the task is completed (completed field is true)
      if (task.completed === true) {
        // Increment the count for the corresponding user id in the 'completed' object
        if (completed[task.userId] === undefined) {
          completed[task.userId] = 1;
        } else {
          completed[task.userId]++;
        }
      }
    }

    // Print the results (an object with user ids as keys and the count of completed tasks as values)
    console.log(completed);
  } else {
    // If the response status code is not 200, log an error message with the status code
    console.log('An error occurred. Status code: ' + response.statusCode);
  }
});
