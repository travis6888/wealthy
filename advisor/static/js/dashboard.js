/**
 * Created by Travis on 11/13/14.
 */
$(document).ready( function(){




$('.loadPort').on('click', function(){
    $.ajax({
        url: '/price_lookup/',
        type: 'GET',
        dataType: 'json',
        success: function(response){
            for (var key in response) {
                var value = response[key];
                $('.quotesData').append("<h2>Buy shares of "+key+" for $" + value+"</h2><button class='btn-xl btn btn-default'>Buy</button>")
                $('.loadPort').toggle();
            }

        },
        error: function(error){
            console.log(error)
        }
    });
    var stocks =  {'names': []};

});








});