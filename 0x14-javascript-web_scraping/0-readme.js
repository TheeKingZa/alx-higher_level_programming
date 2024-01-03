const fs = require('fs');

/**
 * Reads and prints the content of a file.
 * @param {string} filePath -The path of the file to read.
  */
function readFileContent(filePath) {
	// Use fs.readFile to asynchronously read the file content
	// in utf-8 encoding
	fs.readFile(filePath, 'utf-8', (error, data) => {
		if (error) {
			// If an error occurs during reading,
			// print the error object
			console.error(error);
		} else {
			// Print the content of the file
			// if reading is successful
			console.log(data);
		}
	});
}

// Check if the script is called with the correct number of arguments
if (process.argv.length !== 3) {
	// Print an error message if the correct number of arguments 
	// is not provided
	console.error('Usage: node 0-readme.js <file-path>');
    } else {
	    // Extract the file path from the command line arguments
	    const filePath = process.argv[2];
            
	    // Call the function to read and print the content
	    // of the specified file
	    readFileContent(filePath);
    }      
