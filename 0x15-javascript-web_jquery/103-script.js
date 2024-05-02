$(document).ready(function () {
    function translate() {
        let lang = $('#language_code').val();
        $.get(`https://www.fourtonfish.com/hellosalut/?lang=${lang}`, function(data) {
            $('#hello').text(data.hello);
        });
    }

    $('#btn_translate').click(translate);

    $('#language_code').keypress(function (event) {
        if (event.which == 13) {  // Enter key code
            translate();
        }
    });
});
