#!/usr/bin/node
// The above line is a shebang indicating that the script should be run using the specified interpreter, in this case, 'node'.

// Import the 'SquareP' class from the specified module.
const SquareP = require('./5-square');

// Define a class named 'Square' that extends 'SquareP'.
class Square extends SquareP {
  // Method to print a square of characters to the console.
  charPrint (c) {
    // If 'c' is undefined, set it to 'X'.
    if (c === undefined) {
      c = 'X';
    }
    // Iterate over each row (height).
    for (let i = 0; i < this.height; i++) {
      let s = '';
      // Iterate over each column (width) in the current row.
      for (let j = 0; j < this.width; j++) {
        // Concatenate the specified character 'c' to the string.
        s += c;
      }
      // Print the string to the console.
      console.log(s);
    }
  }
}

// Export the 'Square' class as part of the module.
module.exports = Square;
