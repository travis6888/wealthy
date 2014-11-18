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
            console.log(response)
        },
        error: function(error){
            console.log(error)
        }
    });
    var stocks =  {'names': []};
    
});








});