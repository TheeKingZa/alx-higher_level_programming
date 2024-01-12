// Attach a click event handler to the <DIV> element with the id 'toggle_header'
$('DIV#toggle_header').click(function () {
  // Inside the click event handler function:

  // Toggle between the CSS classes 'green' and 'red' for all <HEADER> elements
  $('HEADER').toggleClass('green red');
});
