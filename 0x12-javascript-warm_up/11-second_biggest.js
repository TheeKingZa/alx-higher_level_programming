#!/usr/bin/node
// The above line is a shebang indicating that the script should be run using the specified interpreter, in this case, 'node'.

// Check if there are less than or equal to 3 command-line arguments.
if (process.argv.length <= 3) {
  // If there are not enough arguments, print '0'.
  console.log('0');
} else {
  // If there are enough arguments, execute the following block.

  // Extract numeric values from the command-line arguments starting from the third argument.
  const arr = process.argv.slice(2).map(Number);

  // Sort the array in descending order and retrieve the second element.
  const second = arr.sort(function (a, b) { return b - a; })[1];

  // Print the second largest value to the console.
  console.log(second);
}
