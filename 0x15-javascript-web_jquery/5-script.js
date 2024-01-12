// Attach a click event handler to the <DIV> element with the id 'add_item'
$('DIV#add_item').click(function () {
  // Inside the click event handler function:

  // Append a new <li> element with the text 'Item' to the <UL> with the class 'my_list'
  $('UL.my_list').append('<li>Item</li>');
});
