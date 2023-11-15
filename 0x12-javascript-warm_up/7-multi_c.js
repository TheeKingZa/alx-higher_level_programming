#!/usr/bin/node
// The above line is a shebang indicating that the script should be run using the specified interpreter, in this case, 'node'.

// Check if the first command-line argument is undefined or not a number.
if (process.argv[2] === undefined || isNaN(process.argv[2])) {
  // If it's undefined or not a number, print 'Missing number of occurrences'.
  console.log('Missing number of occurrences');
} else {
  // If a valid number is provided, execute the following block.

  // Convert the first command-line argument to a number.
  const x = Number(process.argv[2]);

  // Initialize a counter variable.
  let i = 0;

  // Loop while the counter is less than the provided number of occurrences.
  while (i < x) {
    // Print 'C is fun' to the console.
    console.log('C is fun');

    // Increment the counter.
    i++;
  }
}
