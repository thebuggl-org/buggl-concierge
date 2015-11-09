//$("#request").click(function (event) {
$("#buggl_form").validate({
    rules: {
        plan: {required: true},
        destination: {required: true, minlength: 3},
        email: {required: true, email: true},
        itinerary: {required: true}
    },
    messages: {
        name: "Don't forget to tell us your name",
        destination: "Please tell us where you wanna go",
        email: "You should enter a valid email address",
        itinerary: "Tell us what you want to do in your trip"

    },
    validClass: "valid",
    errorClass: "invalid",
    errorLabelContainer: "#errores",
    wrapper: "li",
    submitHandler: function (form) {
//        alert("éxito");
//            $("#buggl_form").submit();
        $.post("#", {
            name: $("#name").val(),
            email: $("#email").val(),
            itinerary: $("#itinerary").val(),
            destination: $("#destination").val()

        }).done(function (data) {
            $('#modal1').openModal();//            $("#container_principal").html(data);
        });
    },
    invalidHandler: function (event, validator) {
        // 'this' refers to the form
        var errors = validator.numberOfInvalids();
        if (errors) {
            var message = errors == 1
                    ? 'You missed 1 field.'
                    : 'You missed ' + errors + ' fields. ';
            Materialize.toast(message, 2000)
//            $("#errores").html(message);
            $("div.error").show();
        } else {
            $("div.error").hide();
        }
    }
});
//});

