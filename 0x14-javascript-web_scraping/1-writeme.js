#!/usr/bin/node

const fs = require('fs');

/**
 * Writes a string to a file.
 * @param {string} filePath - The path of the file to write.
 * @param {string} content - The string to write to the file.
 */
function writeToFile(filePath, content) {
    // Use fs.writeFile to asynchronously write content to the specified file path
    // 'utf-8' specifies the encoding of the file content to be written
    // The callback function is executed once the write operation is complete or an error occurs
    fs.writeFile(filePath, content, 'utf-8', function (error) {
        // The callback function receives one parameter: error

        // If there is an error during writing, print the error
        // Otherwise, indicate that the write operation was successful
        if (error) {
            console.error(error);
        } else {
            console.log('The file has been successfully written.');
        }
    });
}

// Check if the script is called with the correct number of arguments
if (process.argv.length !== 4) {
    // Print an error message if the correct number of arguments is not provided
    console.error('Usage: node 1-writeme.js <file-path> <content>');
} else {
    // Extract the file path and content from the command line arguments
    const filePath = process.argv[2];
    const content = process.argv[3];

    // Call the function to write the content to the specified file
    writeToFile(filePath, content);
}
