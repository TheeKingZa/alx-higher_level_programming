// Wait for the HTML document to be fully loaded before executing the script
$(document).ready(function () {
  // Make a GET request to the 'https://fourtonfish.com/hellosalut/?lang=fr' URL
  $.get('https://fourtonfish.com/hellosalut/?lang=fr', function (data) {
    // Inside the callback function:

    // Set the text content of the <DIV> element with the id 'hello' to the retrieved greeting from the API response
    $('DIV#hello').text(data.hello);
  });
});
