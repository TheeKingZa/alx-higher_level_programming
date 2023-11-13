#!/usr/bin/node
// The above line is a shebang indicating that the script should be run using the specified interpreter, in this case, 'node'.

// Check if the first command-line argument is not a number or is undefined.
if (isNaN(process.argv[2]) || process.argv[2] === undefined) {
  // If it's not a number or is undefined, print 'Not a number'.
  console.log('Not a number');
} else {
  // If it's a number, print 'My number:' followed by the parsed integer value of the argument.
  console.log('My number:', parseInt(process.argv[2]));
}
