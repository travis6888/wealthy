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
    $.ajax({
            url: '/find_portfolio/',
            type: 'GET',
            dataType: 'json',

            success: function (stock_response) {
                var stockedname = stock_response.stocksn;
                stocks['names'].push(stockedname.stock1n, stockedname.stock2n, stockedname.stock3n, stockedname.stock4n, stockedname.stock5n);

            },
            error: function (error) {
                console.log(error);

            }

            });
});








});