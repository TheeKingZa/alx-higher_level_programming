#!/usr/bin/node
// The above line is a shebang indicating that the script should be run using the specified interpreter, in this case, 'node'.

// Check if a command-line argument is provided.
if (process.argv[2] === undefined) {
  // If no argument is provided, print 'No argument'.
  console.log('No argument');
} else {
  // If an argument is provided, print the value of the first argument.
  console.log(process.argv[2]);
}
