#!/usr/bin/node
// The above line is a shebang indicating that the script should be run using the specified interpreter, in this case, 'node'.

// Define a class named 'Rectangle'.
class Rectangle {
  // Constructor method to initialize 'width' and 'height'.
  constructor(w, h) {
    // Check if both 'w' and 'h' are greater than 0.
    if ((w > 0) && (h > 0)) {
      // If true, set 'width' and 'height' properties.
      this.width = w;
      this.height = h;
    }
  }
}

// Export the 'Rectangle' class as part of the module.
module.exports = Rectangle;
