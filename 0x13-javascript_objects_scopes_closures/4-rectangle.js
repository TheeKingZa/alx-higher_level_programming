#!/usr/bin/node
// The above line is a shebang indicating that the script should be run using the specified interpreter, in this case, 'node'.

// Define a class named 'Rectangle'.
class Rectangle {
  // Constructor method to initialize 'width' and 'height'.
  constructor (w, h) {
    // Check if both 'w' and 'h' are greater than 0.
    if ((w > 0) && (h > 0)) {
      // If true, set 'width' and 'height' properties.
      this.width = w;
      this.height = h;
    }
  }

  // Method to print a rectangle to the console.
  print () {
    // Iterate over each row (height).
    for (let i = 0; i < this.height; i++) {
      let s = '';
      // Iterate over each column (width) in the current row.
      for (let j = 0; j < this.width; j++) {
        // Concatenate 'X' characters to the string.
        s += 'X';
      }
      // Print the string to the console.
      console.log(s);
    }
  }

  // Method to rotate the rectangle (swap width and height).
  rotate () {
    const aux = this.width;
    this.width = this.height;
    this.height = aux;
  }

  // Method to double the dimensions of the rectangle.
  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

// Export the 'Rectangle' class as part of the module.
module.exports = Rectangle;
