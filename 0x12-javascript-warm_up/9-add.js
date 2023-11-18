#!/usr/bin/node

// Check if the correct number of command-line arguments is provided
if (process.argv.length !== 4) {
  console.error('Usage: ./9-add.js <number1> <number2>');
  process.exit(1); // Exit with a non-zero status to indicate an error
}

// Define a function named 'add' that takes two parameters 'a' and 'b'.
function add(a, b) {
  // Check if inputs are valid numbers
  if (isNaN(a) || isNaN(b)) {
    console.error('Invalid input. Please provide valid numbers.');
    process.exit(1);
  }

  // Calculate the sum of 'a' and 'b' and store it in the variable 'result'.
  const result = a + b;

  // Print the sum to the console.
  console.log(result);
}

// Call the 'add' function, passing the numeric values of the third and fourth command-line arguments.
add(Number(process.argv[2]), Number(process.argv[3]));
