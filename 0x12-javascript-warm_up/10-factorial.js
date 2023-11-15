#!/usr/bin/node
// The above line is a shebang indicating that the script should be run using the specified interpreter, in this case, 'node'.

// Define a function named 'factorial' that takes one parameter 'n'.
function factorial(n) {
  // Check if 'n' is negative.
  if (n < 0) {
    // If 'n' is negative, return -1.
    return (-1);
  }

  // Check if 'n' is 0 or not a number.
  if (n === 0 || isNaN(n)) {
    // If 'n' is 0 or not a number, return 1.
    return (1);
  }

  // If 'n' is a positive number, calculate and return the factorial using recursion.
  return (n * factorial(n - 1));
}

// Call the 'factorial' function, passing the numeric value of the third command-line argument.
console.log(factorial(Number(process.argv[2])));
