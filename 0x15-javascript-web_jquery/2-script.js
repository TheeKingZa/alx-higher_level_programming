// Attach a click event handler to the <DIV> element with the id 'red_header'
$('DIV#red_header').click(function () {
  // Inside the click event handler function:

  // Select all <HEADER> elements and set their text color to red (#FF0000)
  $('HEADER').css('color', '#FF0000');
});
