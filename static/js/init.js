(function ($) {
    $(function () {
        $('.modal-trigger').leanModal();
        $('.button-collapse').sideNav();
        $('.parallax').parallax();
    }); // end of document ready
    $(window).scroll(function () {
        var altura = $("#barra").height();
        if ($(window).scrollTop() > 0) {
            $("#barra").css({"box-shadow": "0 2px 5px 0 rgba(0, 0, 0, 0.16), 0 2px 10px 0 rgba(0, 0, 0, 0.12)", "background-color": "rgba(150,150,150," + 0.3 + ")"});
        } else {
            $("#barra").css({"box-shadow": "none", "background-color": "rgba(150,150,150," + 0 + ")"});
        }



    })
})(jQuery); // end of jQuery name space

$('a[href$="#buggl_form"]').click(function () {
    $('html, body').animate({
        scrollTop: $($.attr(this, 'href')).offset().top - 150
    }, 500);
    return false;
});