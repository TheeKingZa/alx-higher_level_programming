// Attach a click event handler to the <DIV> element with the id 'red_header'
$('DIV#red_header').click(function () {
  // Inside the click event handler function:

  // Add the CSS class 'red' to all <HEADER> elements
  $('HEADER').addClass('red');
});
