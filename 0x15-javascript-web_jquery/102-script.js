// Wait for the document to be ready
$(document).ready(function () {
  // When the user clicks on INPUT#btn_translate
  $('#btn_translate').click(function () {
    // Get the language code from INPUT#language_code
    const languageCode = $('#language_code').val();

    // Fetch the translation using the API
    $.get(`https://www.fourtonfish.com/hellosalut/hello/${languageCode}`, function (data) {
      // Display the translation in DIV#hello
      $('#hello').text(data.hello);
    });
  });
});
