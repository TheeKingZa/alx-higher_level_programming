const myModule = require('./path-to-your-script'); // Replace with the actual path to your script

// Define a function to be called by callMeMoby
function printHello() {
  console.log('Hello!');
}

// Use callMeMoby to call printHello 3 times
myModule.callMeMoby(3, printHello);
