// Add a new element to the list when DIV#add_item is clicked
$('#add_item').click(function() {
  $('UL.my_list').append('<li>Item</li>');
});

// Remove the last element from the list when DIV#remove_item is clicked
$('#remove_item').click(function() {
  $('UL.my_list li:last-child').remove();
});

// Clear all elements from the list when DIV#clear_list is clicked
$('#clear_list').click(function() {
  $('UL.my_list').empty();
});
