


$(document).ready( function() {

    $('.gtPortfolio').on('click', function () {
        $.ajax({
            url: '/income/',
            type: 'GET',
            dataType: 'json',

            success: function (stock_response) {
                $('.portfolioResultsTax').html("<h3>Your after tax income is roughly : $" + stock_response.after_tax);
            },
            error: function (error_response) {
            }
        }).complete(function () {

            $.ajax({
                url: '/rent_to_median/',
                type: 'GET',
                dataType: 'json',

                success: function (stock_response) {
                    console.log(stock_response.percentage_housing);
                    console.log(stock_response.disposible);

                    $('.portfolioResultsMonth').html("<h3>Your disposible income is : $" + stock_response.disposible + "</h3>" +
                        "<h3>You spend " + (stock_response.percentage_housing * 100).toFixed(2) + " % on housing</h3>");


                },
                error: function (error_response) {
                }
            }).complete(function () {
                $.ajax({
                    url: '/find_investment_monthly/',
                    type: 'GET',
                    dataType: 'json',

                    success: function (stock_response) {

                        $('.monthInvestment').html("<h3>Your monthly investment should be : $" + stock_response.invest + "</h3>");
                        var stocks = {'names': []};


                    },
                    error: function (error_response) {
                    }
                }).complete(function () {
                    var stocks ={'names': []};
                    var values = [];
                    var names = [];
                    var portfolio = [];
                    var expected = [];
                    $.ajax({
                        url: '/find_portfolio/',
                        type: 'GET',
                        dataType: 'json',

                        success: function (stock_response) {
                            var stocked = stock_response.stocksp;
                            var stockedname = stock_response.stocksn;
                            $('.gtPortfolio').hide('slow');
                            //
                            values.push(stocked.stock1p, stocked.stock2p, stocked.stock3p, stocked.stock4p, stocked.stock5p);
                            names.push(stockedname.stock1n, stockedname.stock2n, stockedname.stock3n, stockedname.stock4n, stockedname.stock5n);
                            expected.push(stock_response.expected);
                            portfolio.push(stock_response.portfolio);
                            stocks['names'].push(stockedname.stock1n, stockedname.stock2n, stockedname.stock3n, stockedname.stock4n, stockedname.stock5n);
                            $('.getPortfolio').html('<h3>The expected return of this portfolio when your 65 is: $' + stock_response.return);
                            var stock_list = stock_response.stock_list;
                                for (i = 0; i < stock_list.length; i++) {
                                    $('#accordion2').append('<h3>' + stock_list[i].name + '</h3><div>' + stock_list[i].info + '</div>');
                                }
                                $('#accordion2').show();
                                $('#accordion2').accordion({active: 1});

                        },
                        error: function (error_response) {
                        }


                    }).complete(function () {


                        $('.riskScore').hide();
                        var pie = new d3pie("pieChart2", {
                            "header": {
                                "title": {
                                    "text": portfolio,
                                    "color": "fec503",
                                    "fontSize": 28,
                                    "font": "open sans"
                                },
                                "subtitle": {
                                    "text": "Expected return of " + (expected * 100).toFixed(2)+ " % ",

                                    //                    "color": "#fec503",
                                    "fontSize": 15,
                                    "font": "open sans"
                                },
                                "titleSubtitlePadding": 9
                            },
                            "footer": {
                                "color": "#999999",
                                "fontSize": 10,
                                "font": "open sans",
                                "location": "bottom-left"
                            },
                            "size": {
                                "canvasHeight": 400,
                                "canvasWidth": 400,
                                "pieInnerRadius": "9%",
                                "pieOuterRadius": "90%"
                            },
                            "data": {
                                "sortOrder": "value-asc",
                                "content": [
                                    {
                                        "label": names[0],
                                        "value": values[0],
                                        "color": "#1f7f0e"
                                    },
                                    {
                                        "label": names[1],
                                        "value": values[1],
                                        "color": "#2ea217"
                                    },
                                    {
                                        "label": names[2],
                                        "value": values[2],
                                        "color": "#043a00"
                                    },
                                    {
                                        "label": names[3],
                                        "value": values[3],
                                        "color": "#40cb27"
                                    },
                                    {
                                        "label": names[4],
                                        "value": values[4],
                                        "color": "#155d07"
                                    }
                                    //
                                ]
                            },
                            "labels": {
                                "outer": {
                                    "pieDistance": 32
                                },
                                "inner": {

                                    "hideWhenLessThanPercentage": 3
                                },
                                "mainLabel": {
                                    "fontSize": 11
                                },
                                "percentage": {
                                    "color": "#ffffff",
                                    "decimalPlaces": 0
                                },
                                "value": {
                                    "color": "#adadad",
                                    "fontSize": 11
                                },
                                "lines": {
                                    "enabled": true
                                }
                            },
                            "effects": {
                                "pullOutSegmentOnClick": {
                                    "effect": "linear",
                                    "speed": 400,
                                    "size": 8
                                }
                            },
                            "misc": {
                                "gradient": {
                                    "enabled": true,
                                    "percentage": 100
                                }
                            }

                        });


                    });
//                        ;.complete(function () {
//                            var stockInfo = JSON.stringify(stocks);
//                            $.ajax({
//                                url: '/stock_lookup/',
//                                type: 'POST',
//                                dataType: 'json',
//                                data: stockInfo,
//                                success: function (stock_response) {
//                                    var stock_list = stock_response.stock_list1;
//                                    for (i = 0; i < stock_list.length; i++) {
//
//
//                                        var stocks_prices = $('.stockPrices');
//                                        $(stocks_prices).append('<h3 class="stPrice">   ' + stocks['names'][i] + '   </h3>  ');
//                                        $(stocks_prices).append('<p class="stPrice">Recent stock price:  ' + stock_list[i].stock_price + '   </p>  ');
////
//
//
//                                    }
//                                },
//                                error: function (error_response) {
//                                }
//                            });
//                        });
                    });
                });
            });
        });
//    });

//    Toggle buttons for questions
    $('.questSetOneNext').on('click', function () {
        $('.questSetOne').hide('slow');
        $('.questSetTwo').show('slow');
    });

    $('.questSetTwoNext').on('click', function () {
        $('.questSetTwo').hide('slow');
        $('.questSetThree').show('slow');
    });
    $('.questSetThreeNext').on('click', function () {
        $('.questSetThree').hide('slow');
        $('.questSetFour').show('slow');
    });



// Demo setup ajax
    $('.demo').on('click', function () {
        $('.demoAgeInput').toggle();
        $('.ageInputBtn').toggle();

    });
    $('.ageInputBtn').on('click', function () {

        $('.demoHide').toggle('slow');
        $('.demoAgeInput').toggle();
        $('.ageInputBtn').toggle();

        var pie = new d3pie("pieChart", {
            "header": {
                "title": {
                    "text": "Conservative Portfolio",
                    "color": "fec503",
                    "fontSize": 28,
                    "font": "open sans"
                },
                "subtitle": {
                    "text": "Expected return of 5.8% ",

//                    "color": "#fec503",
                    "fontSize": 15,
                    "font": "open sans"
                },
                "titleSubtitlePadding": 9
            },
            "footer": {
                "color": "#999999",
                "fontSize": 10,
                "font": "open sans",
                "location": "bottom-left"
            },
            "size": {
                "canvasHeight": 400,
                "canvasWidth": 400,
                "pieInnerRadius": "9%",
                "pieOuterRadius": "90%"
            },
            "data": {
                "sortOrder": "value-desc",
                "content": [
                    {
                        "label": "S&P500 Index ETF",
                        "value": 30,
                        "color": "#1f7f0e"
                    },
                    {
                        "label": "REIT ETF",
                        "value": 10,
                        "color": "#2ea217"
                    },
                    {
                        "label": "Utilities ETF",
                        "value": 10,
                        "color": "#043a00"
                    },
                    {
                        "label": "Government Bonds",
                        "value": 15,
                        "color": "#40cb27"
                    },
                    {
                        "label": "LT CRP BNDs",
                        "value": 15,
                        "color": "#155d07"
                    },
                    {
                        "label": "INT CRP BNDs",
                        "value": 20,
                        "color": "#0e4904"
                    }
                ]
            },
            "labels": {
                "outer": {
                    "pieDistance": 32
                },
                "inner": {
                    "hideWhenLessThanPercentage": 3
                },
                "mainLabel": {
                    "fontSize": 11
                },
                "percentage": {
                    "color": "#ffffff",
                    "decimalPlaces": 0
                },
                "value": {
                    "color": "#adadad",
                    "fontSize": 11
                },
                "lines": {
                    "enabled": true
                }
            },
            "effects": {
                "pullOutSegmentOnClick": {
                    "effect": "linear",
                    "speed": 400,
                    "size": 8
                }
            },
            "misc": {
                "gradient": {
                    "enabled": true,
                    "percentage": 100
                }
            }
        });

        var ageInput = $('.demo_age').val();
        var age = {};
        age['data'] = ageInput;
        var stockInfo = JSON.stringify(age);
        $.ajax({
            url: '/demo_age/',
            type: 'POST',
            dataType: 'json',
            data: stockInfo,
            success: function (stock_response) {
                $('.userAge').html('<h3 class="section-subheading text-muted "> ' + stock_response.age + ' years old and ' +
                    'a medium convservative investor</h3>');
                $('.demoResults').html("<h3>Here is your outlook for the next " + (70 - stock_response.age) + " years!" +
                    "</h3><br><h3>Expected portfolio value at 65 years old:<br> $" + stock_response.return + "</h3>" +
                    "<br><h3>You should invest $ " + "" + stock_response.investment + " a month </h3>" +
                    "<br><h3>Which is " + ((stock_response.investment / 4000) * 100) + " % of your monthly income</h3>");

            },
            error: function (error_response) {
            }
        }).complete(function () {
            $('#accordion').accordion({active: 1,
    header: "h3",
    collapsible: true,
    autoHeight: false,
    navigation: true
});

        });

//Register modal switches
        $(document).on('click', '#usernameNext', function () {
            $('.userName').hide();
            $('.emailPassword').fadeIn('slow');


        });
        $(document).on('click', '.emailPasswordNext', function () {
            $('.emailPasswordNext').hide();
            $('.demographics').fadeIn('slow');
            $('.doneButton').fadeIn('slow');


        });


    });
});




