#!/usr/bin/node
// The above line is a shebang indicating that the script should be run using the specified interpreter, in this case, 'node'.

// Define a class named 'Rectangle'.
class Rectangle {
  // Constructor method to initialize 'width' and 'height'.
 constructor (w, h) {
    this.width = w;
    this.height = h;
  }
}

// Export the 'Rectangle' class as part of the module.
module.exports = Rectangle;
