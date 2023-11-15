#!/usr/bin/node
// The above line is a shebang indicating that the script should be run using the specified interpreter, in this case, 'node'.

// Export a function named 'add' as part of the module.
exports.add = function (a, b) {
  // Return the sum of 'a' and 'b'.
  return (a + b);
};
