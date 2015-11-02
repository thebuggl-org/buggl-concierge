/**
 * selects the radio button
 */
$("#a-basic").click(
        function () {
            $("#basic").prop("checked", true);
        }
);
$("#a-premier").click(
        function () {
            $("#premier").prop("checked", true);
        }
);
$("#a-elite").click(
        function () {
            $("#elite").prop("checked", true);
        }
);

/**
 * Scrolls softly to the next step in the form, and shows the clicked item as the
 * selected one
 */
$('#buggl_form a').click(function () {
    $('#buggl_form a').children().addClass("unchecked");
    $('#buggl_form a').children().removeClass("checked");
    $(this).children(':first').addClass("checked");
    $(this).children(':first').removeClass("unchecked");
    
    $('html, body').animate({
        scrollTop: $($.attr(this, 'href')).offset().top - 90
    }, 500);
    return false;
});