// Wait for the document to be ready
$(document).ready(function () {
  // Function to fetch and display the translation
  function fetchTranslation() {
    // Get the language code from INPUT#language_code
    const languageCode = $('#language_code').val();

    // Fetch the translation using the API
    $.get(`https://www.fourtonfish.com/hellosalut/hello/${languageCode}`, function (data) {
      // Display the translation in DIV#hello
      $('#hello').text(data.hello);
    });
  }

  // When the user clicks on INPUT#btn_translate
  $('#btn_translate').click(function () {
    fetchTranslation();
  });

  // When the user presses ENTER in INPUT#language_code
  $('#language_code').keypress(function (e) {
    if (e.which === 13) { // Check if the pressed key is ENTER
      fetchTranslation();
    }
  });
});
