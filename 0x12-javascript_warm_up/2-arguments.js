#!/usr/bin/node
// The above line is a shebang indicating that the script should be run using the specified interpreter, in this case, 'node'.

// Check the number of command-line arguments.
if (process.argv.length === 2) {
  // If there are no arguments (only the script name), print 'No argument'.
  console.log('No argument');
} else if (process.argv.length === 3) {
  // If there is one argument (in addition to the script name), print 'Argument found'.
  console.log('Argument found');
} else {
  // If there are more than one argument, print 'Arguments found'.
  console.log('Arguments found');
}
