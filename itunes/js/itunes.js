$.validator.setDefaults({
    submitHandler: function() { alert("submitted!"); }
});

$().ready(function() {
    
    $('.btn-add-rules-row').live("click", null, addRule);
    $('.btn-rm-rules-row').live("click", null, rmRule);
        
    /* Handle rule list + and - buttons */
    function addRule(event) {
        $('.rules-list').append($($('.rules-list .rule')[0]).clone());
        return false;
    };
    function rmRule(event) {
        if ($('.rules-list').children().length > 1) {
            $(event.target.parentNode).remove()
        }
        return false;
    };

    jQuery.validator.addMethod("match_checked", function(value, element) {
        if ($(element).is(":checked")) {
                var matched = true;
                $('.match_query').each(function(elem) {
                    if (!$(elem).is(":filled")) {
                        matched = false;
                    }
                });
                return matched;
        }
        return true;
        
    }, "You have checked match so you must enter at least one query.");


    jQuery.validator.addMethod("limit_checked", function(value, element) {
        if ($("#limit_to").is(":checked")) {
                if ($("#limit_amount").is(":filled")) {
                    return true;
                }
                return false;
        }
        return true;
    }, "You have checked limit to but not entered a number!");

    $("#smartPlaylist").validate({
        invalidHandler: function(e, validator) {
            var errors = validator.numberOfInvalids();
            if (errors) {
                var message = errors == 1
                    ? 'You missed 1 field. It has been highlighted below'
                    : 'You missed ' + errors + ' fields.  They have been highlighted below';
                $("div.error span").html(message);
                $("div.error").show();
            } else {
                $("div.error").hide();
            }
        },
        submitHandler: function(form) {
           alert("validated!");
           form.submit();
        }
    });

});