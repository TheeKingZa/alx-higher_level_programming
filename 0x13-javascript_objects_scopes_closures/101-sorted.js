#!/usr/bin/node
const dict = require('./101-data').dict;

// Convert the original dictionary into an array of key-value pairs
const totalist = Object.entries(dict);

// Extract the values from the original dictionary
const vals = Object.values(dict);

// Get unique values using a Set
const valsUniq = [...new Set(vals)];

// Create a new dictionary
const newDict = {};

// Iterate over unique values
for (const j in valsUniq) {
  // Create a list to store keys for the current unique value
  const list = [];

  // Iterate over key-value pairs
  for (const k in totalist) {
    // If the value matches the current unique value, add the key to the list
    if (totalist[k][1] === valsUniq[j]) {
      list.unshift(totalist[k][0]);
    }
  }

  // Assign the list to the new dictionary with the unique value as the key
  newDict[valsUniq[j]] = list;
}

// Print the new dictionary
console.log(newDict);

