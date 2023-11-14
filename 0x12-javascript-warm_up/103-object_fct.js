#!/usr/bin/node
// The above line is a shebang indicating that the script should be run using the specified interpreter, in this case, 'node'.

// Create an object named 'myObject' with properties 'type' and 'value'.
const myObject = {
  type: 'object',
  value: 12
};

// Print the initial state of 'myObject' to the console.
console.log(myObject);

// Add a method named 'incr' to 'myObject' that increments the 'value' property.
myObject.incr = function () {
  // 'this' refers to the object (myObject) to which the method is attached.
  this.value++;
};

// Invoke the 'incr' method, which increments the 'value' property.
myObject.incr();
// Print the state of 'myObject' after the first increment.
console.log(myObject);

// Invoke 'incr' again.
myObject.incr();
// Print the state of 'myObject' after the second increment.
console.log(myObject);

// Invoke 'incr' once more.
myObject.incr();
// Print the state of 'myObject' after the third increment.
console.log(myObject);
