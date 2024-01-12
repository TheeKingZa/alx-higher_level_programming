// Make a GET request to the 'https://swapi.co/api/people/5/?format=json' URL
$.get('https://swapi.co/api/people/5/?format=json', function (data) {
  // Inside the callback function:

  // Set the text content of the <DIV> element with the id 'character' to the retrieved name from the API response
  $('DIV#character').text(data.name);
});
