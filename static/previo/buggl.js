//$("#request").click(function (event) {
$("#buggl_form").validate({
    rules: {
        name: {required: true, minlength: 3},
        email: {required: true, email: true},
        plan: {required: true}
    },
    messages: {
        name: "Don't forget to tell us your name",
        email: "You should enter a valid email address",
        plan: "Don't forget to choose a plan"

    },
    validClass: "valid",
    errorClass: "invalid",
    errorLabelContainer: "#errores",
    wrapper: "li",
    submitHandler: function (form) {
        
        $.post( "#", { 
            name: $("#name").val(), 
            email:$("#email").val(),
            trip_category:$("#trip_category").val(),
            plan:$("input[name=plan]:checked").val()
            
        }).done(function( data ) {
               $( "#container_principal" ).html( data );
        });
        
    },
    invalidHandler: function (event, validator) {
        // 'this' refers to the form
        var errors = validator.numberOfInvalids();
        if (errors) {
            var message = errors == 1
                    ? 'You missed 1 field.'
                    : 'You missed ' + errors + ' fields. ';
            Materialize.toast(message, 2000);
//            $("#errores").html(message);
            $("div.error").show();
        } else {
            $("div.error").hide();
        }
    }
});


// $("#request").onclick(function(){
   
// })
    
    

//});

