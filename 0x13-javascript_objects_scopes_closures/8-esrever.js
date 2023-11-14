#!/usr/bin/node

exports.esrever = function (list) {
  // Check if the list is not empty or not an array
  if (!Array.isArray(list) || list.length === 0) {
    return list;
  }

  // Swap elements from the beginning and end of the array
  for (let i = 0, j = list.length - 1; i < j; i++, j--) {
    // Use a temporary variable to swap elements
    const temp = list[i];
    list[i] = list[j];
    list[j] = temp;
  }

  return list;
};
