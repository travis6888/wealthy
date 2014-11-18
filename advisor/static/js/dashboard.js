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
            console.log(response.stocks);
//
//            for(i = 0; i < response.length; i++) {
//
//
for (var key in response) {
 console.log(response[key][Object.keys(response[key])[0]]); // 81.25
}


        },
        error: function(error){
            console.log(error)
        }
    });
    var stocks =  {'names': []};

});








});