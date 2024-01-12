// Attach a click event handler to the <DIV> element with the id 'update_header'
$('DIV#update_header').click(function () {
  // Inside the click event handler function:

  // Set the text content of all <HEADER> elements to 'New Header!!!'
  $('HEADER').text('New Header!!!');
});
