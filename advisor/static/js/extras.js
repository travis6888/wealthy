   $(document).ready(function () {
       var apiKey = 'TsF9wdpdkj4SGE6BCHyk';


       $('.quoteLookup').on('click', function () {
           var searchQuery = $('#searchQuotes').val();
           $.ajax({
               url: 'http://www.quandl.com/api/v1/datasets/WIKI/' + searchQuery + '.json?trim_start=2012-05-17&trim_end=2014-07-24&auth_token=TsF9wdpdkj4SGE6BCHyk',
               type: 'GET',
               dataType: 'json',
               success: function (stock_response) {
                   var stock = stock_response.data[0][1];
                   var info = stock_response.description;

               },
               error: function (error_response) {
               }
           });
       });
       $('.lookup').on('click', function () {
           var searchQuery = $('#searchQuotes').val();
           $.ajax({
               url: 'http://dev.markitondemand.com/Api/v2/Quote/jsonp?symbol=' + searchQuery + '&callback=myFunction',
               type: 'GET',
               dataType: 'json',
               success: function (stock_response) {
                   var stock = stock_response.data[0][1];
               },
               error: function (error_response) {
               }
           });
       });

       $('.zipsaleHomeLookupMedHome').on('click', function () {
           var zipcode = $('.zipLookupMedHome').val();
           var country = $('#countryInput').val();
           var state = $('#stateInput').val();
           $.ajax({
               url: 'http://www.quandl.com/api/v1/datasets/ZILLOW/MZIP_MEDIANSOLDPRICE_ALLHOMES_' + zipcode + '.json',
               type: 'GET',
               dataType: 'json',
               success: function (zip_response) {
                   var date = zip_response.data[0][0];
                   var price = zip_response.data[0][1];
                   $('.response').append('<div><p> Recent date:' + date + '</p><p>Median price:' + price + '</p></div>');
                   $('.zestimates').toggle();
                   $('.getMortgageInfo').toggle();

               },
               error: function (error_response) {
               }
           });

       });

       $('.zipsaleHomeLookupMedHome2').on('click', function () {
           var zipcode = $('.zipLookupMedHome2').val();
           var country = $('#countryInput').val();
           var state = $('#stateInput').val();
           $.ajax({
               url: 'http://www.quandl.com/api/v1/datasets/ZILLOW/MZIP_MEDIANSOLDPRICE_ALLHOMES_' + zipcode + '.json',
               type: 'GET',
               dataType: 'json',
               success: function (zip_response) {
                   var date = zip_response.data[0][0];
                   var price = zip_response.data[0][1];
                   $('.response').append('<div><p> Recent date:' + date + '</p><p>Median price:' + price + '</p></div>');

               },
               error: function (error_response) {
               }
           });

       });
       $('.zipRentLookup').on('click', function () {
           var zipcode = $('.zipLookUpMedRent').val();
           var country = $('#countryInput').val();
           var state = $('#stateInput').val();
           $.ajax({
               url: 'http://www.quandl.com/api/v1/datasets/ZILLOW/RZIP_MEDIANRENTALPRICE_ALLHOMES_' + zipcode + '.json',
               type: 'GET',
               dataType: 'json',
               success: function (zip_response) {
                   var date = zip_response.data[0][0];
                   var price = zip_response.data[0][1];
                   $('.IWantToMove').append('<p> Recent date:' + date + '</p><p>Median price:' + price + '</p>');

               },
               error: function (error_response) {
               }
           });

       });
       $('.rentSubmit').on('click', function () {
           var zipcode = $('.zipcodeRentCalc').val();
           var medianPrice = {};
           $.ajax({
               url: 'http://www.quandl.com/api/v1/datasets/ZILLOW/RZIP_MEDIANRENTALPRICE_ALLHOMES_' + zipcode + '.json',
               type: 'GET',
               dataType: 'json',
               success: function (zip_response) {
//                   for(i = 0; i < zip_response.data[0][i].length; i++){
//
//                   }
                   var date = zip_response.data[0][0];
                   var price = zip_response.data[0][1];
                   var price2 = zip_response.data[1][1];
                   var price3 = zip_response.data[2][1];
                   var price4 = zip_response.data[3][1];

                   var newPrice = (price + price2 + price3+ price4) / 4;
                   $('.IWantToMove').append('<p> Recent date:' + date + '</p><p>Median price:' + newPrice + '</p>');
                   medianPrice['median'] = newPrice;

               },
               error: function (error_response) {
               }
           }).complete(function () {

               var rentInput = $('.rentInput').val();
               console.log(rentInput);

               var rent = {};
               rent['data'] = rentInput;
               var stockInfo = JSON.stringify({'rent': rent, 'medianPrice': medianPrice});

               $.ajax({
                   url: '/rent_to_median/',
                   type: 'POST',
                   dataType: 'json',
                   data: stockInfo,
                   success: function (stock_response) {
                   },
                   error: function (error_response) {
                   }
               });

           })
       });


       $('.mortgageSubmit').on('click', function () {
           var mortgageInput = $('.mortgageInput').val();
           console.log(mortgageInput);
           var mortgage = {};
           mortgage['data'] = mortgageInput;
           var stockInfo = JSON.stringify(mortgage);
           $.ajax({
               url: '/rent_percentage/',
               type: 'POST',
               dataType: 'json',
               data: stockInfo,
               success: function (stock_response) {
               },
               error: function (error_response) {
               }
           });
       });
   });


    $('.quoteLookup').on('click', function () {
        var searchQuery = $('#searchQuotes').val();
        stocked = {};
        stocked['data'] = searchQuery;
        var stockInfo = JSON.stringify(stocked);
        $.ajax({
            url: '/stock_lookup/',
            type: 'POST',
            dataType: 'json',
            data: stockInfo,
            success: function (stock_response) {
                var price = stock_response.stock_price;
                var fiftytwoHigh = stock_response.fiftytwo_week_high;
                var fiftytwoLow = stock_response.fiftytwo_week_low;
                var dividend_yeild = stock_response.dividend_yield;
                var dividend = stock_response.dividend_per_share;


                var stocks = $('.stocks');
                $(stocks).append('<p>Last stock price: ' + price + '</p>');
                $(stocks).append('<p>52 week High: ' + fiftytwoHigh + '</p>');
                $(stocks).append('<p>52 week Low: ' + fiftytwoLow + '</p>');
                $(stocks).append('<p>Yield: ' + dividend_yeild + '%</p>');
                $(stocks).append('<p>Dividend per share: $' + dividend + '</p>');

            },
            error: function (error_response) {
            }
        });
    });
$('.homeOwnerQuestionYes').on('click', function () {
        $('.homeownerQuestions').toggle();
        $('.homeowner').toggle();

    });

    $('.zestimate').on('click', function () {
        $('.zestimateWidget').toggle();
    });

    $('.HomeOwnerQuestionNo').on('click', function () {
        $('.homeownerQuestions').toggle();
        $('.renter').toggle()
    });

    $('.wantToOwn').on('click', function () {
        $('.renter').toggle();

        $('.wantToOwnHome').toggle()
    });
    $('.dontWantToOwn').on('click', function () {
        $('.renter').toggle();
        $('.dontWantToOwnHome').toggle()
    });
    $('.YesMove').on('click', function () {
        $('.dontWantToOwnHome').toggle();
        $('.IWantToMove').toggle()
    });
    $('.NoMove').on('click', function () {
        $('.dontWantToOwnHome').toggle();
        $('.notMove').toggle()
    });
    $('.yesZestimate').on('click', function () {
        $('.questions').toggle();

        $('.zestimates').toggle()
    });
    $('.noZestimate').on('click', function () {
        $('.questions').toggle();

        $('.getMortgageInfo').toggle();
    });