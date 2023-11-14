#!/usr/bin/node
// The above line is a shebang indicating that the script should be run using the specified interpreter, in this case, 'node'.

// Initialize a counter variable.
let narg = 0;

// Export a function named 'logMe'.
exports.logMe = function (item) {
  // Log the item along with the counter.
  console.log(narg + ': ' + item);

  // Increment the counter for the next call.
  narg++;
};

