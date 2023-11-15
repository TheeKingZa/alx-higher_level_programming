#!/usr/bin/node
// The above line is a shebang indicating that the script should be run using the specified interpreter, in this case, 'node'.

// Define a function named 'add' that takes two parameters 'a' and 'b'.
function add (a, b) {
  // Calculate the sum of 'a' and 'b' and store it in the variable 'c'.
  const c = a + b;

  // Print the sum to the console.
  console.log(c);
}

// Call the 'add' function, passing the numeric values of the third and fourth command-line arguments.
add(Number(process.argv[2]), Number(process.argv[3]));
