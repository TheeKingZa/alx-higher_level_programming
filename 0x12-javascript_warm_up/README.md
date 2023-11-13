 JavaScript - Warm up
 ---------------------
 0x12
 ----

 NEED TO KNOW?
 --------------
- [Why JavaScript programming is amazing?](#why-JavaScript-programming-is-amazing)
- [How to run a JavaScript?](#how-to-run-a-javascript-script)
- [How to create variables and constants?](#how-to-create-variables-and-constants)
- [What are differences between var, const and let?](#differences-between-var-const-and-let)
- [What are all the data types available in JavaScript?](#what-are-all-the-data-types-available-in-JavaScript)
- [How to use the if, if ... else statements?](#how-to-use-the-if,-if-...-else-statements)
- [How to use comments?](#how-to-use-comments)
- [How to affect values to variables?](#how-to-affect-values-to-variables)
- [How to use while and for loops?](#how-to-use-while-and-for-loops)
- [How to use break and continue statements?](#how-to-use-break-and-continue-statements)
- [What is a function and how do you use functions?](#what-is-a-function-and-how-do-you-use-functions)
- [What does a function that does not use any return statement return?](#what-does-a-function-that-does-not-use-any-return-statement-return)
- [Scope of variables?](#scope-of-variables)
- [What are the arithmetic operators and how to use them?](#arithmetic-operators-and-how-to-use-them)
- [How to manipulate dictionary?](#how-to-manipulate-dictionary)
- [How to import a file?](#how-to-import-a-file)

-----------------------------------------------------------------------------

# Why JavaScript Programming is Amazing?
  JavaScript is an incredibly versatile programming language that runs in web browsers, making it an essential tool for web development. Its ability to create dynamic and interactive web pages makes it a powerful language in the world of front-end and back-end development.

- [back to top](#need-to-know)
-----------------------------------

#  How to Run a JavaScript Script?
  To run a JavaScript script, you can use a web browser console, Node.js runtime, or an integrated development environment (IDE) like Visual Studio Code. For web browsers, you can include your script in an HTML file and open it in a browser.

javajs
==Code==

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>My JavaScript Page</title>
    <script src="myscript.js"></script>
</head>
<body>
    <!-- Your HTML content here -->
</body>
</html>

- [back to top](#need-to-know)
------------------------------------

# How to Create Variables and Constants?
  In JavaScript, you can create variables using var, let, or const keywords.

javajs
==Code==

// Variable
var x = 10;

// Constant
const PI = 3.14;

// Let (block-scoped variable)
let message = "Hello, World!";


- [back to top](#need-to-know)
---------------------------------------------

# Differences Between var, const and let?
  - var: Function-scoped variable.
  - const: Constant variable that cannot be re-assigned.
  - let: Block-scoped variable that can be re-assigned.

# Data Types in JavaScript?
  JavaScript has several data types, including:
    - Number.
    - String.
    - Boolean.
    - Object.
    - Array.
    - Null.
    - Undefined.

  - [back to top](#need-to-know)
----------------------------------------------------

# How to Use if, if...else Statements?
  Conditional statements allow you to make decisions in your code.

Javascript
==Code==

let x = 10;

if (x > 5) {
    console.log("x is greater than 5");
} else {
    console.log("x is less than or equal to 5");
}


- [back to top](#need-to-know)
--------------------------------------------------------------------------

# How to Use Comments?
Comments in JavaScript are crucial for code readability.
Use // for single-line comments 
and /* */ for multi-line comments.

javasript
==Code==

// This is a single-line comment

/*
   This is a multi-line comment
   that spans multiple lines
*/


- [back to top](#need-to-know)
---------------------------------------------------------------------------

# How to Affect Values to Variables?
  javascript
  ==Code==

  let x = 5;
x = x + 3; // x now holds the value 8


- [back to top](#need-to-know)
---------------------------------------------------------------------------


# How to use while and for loops?
  Loops help you repeat actions in your code.

--java script--
==Code==

// While Loop
let i = 0;
while (i < 5) {
    console.log(i);
    i++;
}

// For Loop
for (let j = 0; j < 5; j++) {
    console.log(j);
}

- [back to top](#need-to-know)
----------------------------------------------------------------------------

# How to Use break and continue Statements?
  break is used to exit a loop, and continue is used to skip the current iteration and move to the next one.

javascript
==code==

for (let i = 0; i < 10; i++) {
    if (i === 5) {
        break; // Exit the loop when i is 5
    }
    console.log(i);
}

for (let i = 0; i < 10; i++) {
    if (i === 5) {
        continue; // Skip the iteration when i is 5
    }
    console.log(i);
}


- [back to top](#need-to-know)
-----------------------------------------------------------------------------

# What is a Function and How to Use Functions?
  Functions in JavaScript allow you to encapsulate a block of code for reuse.

javascript 
==Code==

function greet(name) {
    console.log("Hello, " + name + "!");
}

greet("John");


- [back to top](#need-to-know)
-----------------------------------------------------------------------------

# What Does a Function That Does Not Use any Return Statement Return?
  A function without a return statement returns undefined by default.

javasript
==Code==

function noReturn() {
    // No return statement
}

let result = noReturn();
console.log(result); // Outputs: undefined

- [back to top](#need-to-know)
-----------------------------------------------------------------------------

# Scope of Variables?
  Variables in JavaScript have function scope (for var) or block scope (for let and const).

javascript
==Code==

if (true) {
    var localVar = "I am a var"; // Function-scoped
    let blockVar = "I am a let"; // Block-scoped
}

console.log(localVar); // Works
console.log(blockVar); // ReferenceError: blockVar is not defined

- [back to top](#need-to-know)
-----------------------------------------------------------------------------

# Arithmetic Operators and How to Use Them? 
  JavaScript supports various arithmetic operators for numerical operations.

javascript
==Code==

let a = 5;
let b = 3;

let sum = a + b;
let difference = a - b;
let product = a * b;
let quotient = a / b;
let remainder = a % b;

- [back to top](#need-to-know)
-----------------------------------------------------------------------------

# How to Manipulate Dictionary?
  JavaScript objects can be used as dictionaries.

javascript
==Code==

let person = {
    name: "John",
    age: 30,
    city: "New York"
};

console.log(person.name); // Outputs: John

- [back to top](#need-to-know)
-----------------------------------------------------------------------------

# How to Import a File?
  In browser-based JavaScript, you can include other scripts using the script tag in HTML. For Node.js, you can use require or import statements.

javascript
==Code==

// Node.js
const otherModule = require('./otherModule');

// ES6 import
import { someFunction } from './anotherModule';

-----------------------------------------------------------------------------

Feel free to explore these concepts further by experimenting with code examples and building small projects.

Happy coding!
-------------
- [back to top](#need-to-know)
