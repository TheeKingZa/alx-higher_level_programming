#!/usr/bin/node
// The above line is a shebang indicating that the script should be run using the specified interpreter, in this case, 'node'.

// Export a function named 'nbOccurrences'.
exports.nbOccurences = function (list, searchElement) {
  // Initialize a variable to count occurrences.
  let nOccurrences = 0;

  // Iterate through the elements of the array.
  for (let i = 0; i < list.length; i++) {
    // Check if the current element is equal to the 'searchElement'.
    if (searchElement === list[i]) {
      // If true, increment the occurrence counter.
      nOccurrences++;
    }
  }

  // Return the total number of occurrences.
  return nOccurrences;
};
