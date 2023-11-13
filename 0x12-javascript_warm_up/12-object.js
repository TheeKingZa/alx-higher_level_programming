#!/usr/bin/node
// The above line is a shebang indicating that the script should be run using the specified interpreter, in this case, 'node'.

// Create an object named 'myObject' with properties 'type' and 'value'.
const myObject = {
  type: 'object',
  value: 12
};

// Print the initial state of the 'myObject' to the console.
console.log(myObject);

// Modify the 'value' property of 'myObject'.
myObject.value = 89;

// Print the updated state of the 'myObject' to the console.
console.log(myObject);
