#!/usr/bin/node
// The above line is a shebang indicating that the script should be run using the specified interpreter, in this case, 'node'.

// Import the 'Rectangle' class from the specified module.
const Rectangle = require('./4-rectangle');

// Define a class named 'Square' that extends 'Rectangle'.
class Square extends Rectangle {
  // Constructor method for the 'Square' class.
  constructor(size) {
    // Call the constructor of the parent class ('Rectangle') with 'size' as both width and height.
    super(size, size);
  }
}

// Export the 'Square' class as part of the module.
module.exports = Square;

