/**
 * Created by Travis on 11/13/14.
 */
$(document).ready(function () {

    var names = [];

    var stocks = {'names': []};
    var totalValue = 0;

    var personalValues = {};
    var portfolioValue = [];
    var portfolioNames = [];



    $('.loadPort').on('click', function () {
        var values = [];
        var portfolio = [];
        var expected = [];
//                    Get all the portfolio information after the user has a risk score
        $.ajax({
            url: '/find_portfolio/',
            type: 'GET',
            dataType: 'json',

            success: function (stock_response) {
                var stocked = stock_response.stocksp;
                var stockedname = stock_response.stocksn;

                values.push(stocked.stock1p, stocked.stock2p, stocked.stock3p, stocked.stock4p, stocked.stock5p);
                names.push(stockedname.stock1n, stockedname.stock2n, stockedname.stock3n, stockedname.stock4n, stockedname.stock5n);
                expected.push(stock_response.expected);
                portfolio.push(stock_response.portfolio);
                stocks['names'].push(stockedname.stock1n, stockedname.stock2n, stockedname.stock3n, stockedname.stock4n, stockedname.stock5n);
            },
            error: function (error_response) {
            }


        }).complete(function () {

            $(function () {

                // Radialize the colors
                Highcharts.getOptions().colors = Highcharts.map(Highcharts.getOptions().colors, function (color) {
                    return {
                        radialGradient: { cx: 0.5, cy: 0.3, r: 0.7 },
                        stops: [
                            [0, color],
                            [1, Highcharts.Color(color).brighten(-0.3).get('rgb')] // darken
                        ]
                    };
                });
            });
            // Build the chart
            $('#pieChartPort').highcharts({
                chart: {
                    plotBackgroundColor: null,
                    plotBorderWidth: null,
                    plotShadow: false
                },
                title: {
                    text: portfolio
                },
                "subtitle": {
                    "text": "Expected return of " + (expected * 100).toFixed(2) + " % "},
                tooltip: {
                    pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
                },
                plotOptions: {
                    series: {
                animation: {
                    duration: 2000,
                    easing: 'easeOutExpo'
                }
            },
                    pie: {
                        allowPointSelect: true,
                        cursor: 'pointer',
                        dataLabels: {
                            enabled: false,
                            format: '<b>{point.name}</b>: {point.percentage:.1f} %',
                            style: {
                                color: (Highcharts.theme && Highcharts.theme.contrastTextColor) || 'black'
                            },
                            connectorColor: 'silver'

                        },
                        showInLegend: true

                    }
                },
                series: [
                    {
                        type: 'pie',
                        name: portfolio,
                        data: [
                            [names[0], values[0]],

                            {
                                name: names[1],
                                y: values[1],
                                sliced: true,
                                selected: true
                            },
                            [names[2], values[2]],
                            [names[3], values[3]],
                            [names[4], values[4]]


                        ]
                    }
                ]

            });


        }).complete(function () {
            $('.loadPort').toggle();

            $.ajax({
                url: '/price_lookup/',
                type: 'GET',
                dataType: 'json',
                success: function (response) {
                    for (var key in response) {
                        var value = response[key];

                        $('.quotesData').append("<button class='btn-lg btn btn-default stocks' data-title=" + value + ">" + key + "</button>")
                    }

                },
                error: function (error) {
                    console.log(error);
                    $('.loadPort').toggle();

                }
            });

        }).complete(function(){
            $.ajax({
                url: '/personal_pie_info/',
                type: 'GET',
                dataType: 'json',

                success: function (stock_response) {
                    console.log(stock_response);
                    totalValue =0;
                    for (var key in stock_response) {
                        var value = stock_response[key];
                        console.log(key);
                        console.log(value);
                        portfolioNames.push(key);
                        portfolioValue.push(value);
                        totalValue += value;


                    }
                $('#pieChartPers').highcharts({
            chart: {
                plotBackgroundColor: null,
                plotBorderWidth: null,
                plotShadow: false
            },
            title: {
                text: 'Your Personal Portfolio'
            },
            "subtitle": {
                "text": "Current Value $"+Number((totalValue).toFixed(2)).toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",")},
            tooltip: {
                pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
            },
            plotOptions: {
                 series: {
                animation: {
                    duration: 2000,
                    easing: 'easeOutExpo'
                }
            },
                pie: {
                    allowPointSelect: true,
                    cursor: 'pointer',
                    dataLabels: {
                        enabled: false,
                        format: '<b>{point.name}</b>: {point.percentage:.1f} %',
                        style: {
                            color: (Highcharts.theme && Highcharts.theme.contrastTextColor) || 'black'
                        },
                        connectorColor: 'silver'

                    },
                    showInLegend: true

                }
            },
            series: [
                {
                    type: "pie",
                    name: 'Stocks',
                    data: (function () {
                        // generate an array of random data
                        var data = [],
                            i;

                        for (i = 0; i < portfolioNames.length; i++) {
                            console.log(portfolioNames[i]);
                            data.push([
                                portfolioNames[i], portfolioValue[i]
                            ]);
                        }
                        return data;
                    }())
                }
            ]

                });
                },
                error: function (error) {
                    console.log(error);
                }
            });
        });
    });

    var personalValues2 = [];
    $('.quotesData').on('click', 'button', function () {
         var totalValue = 0;

    var personalValues = {};
    var portfolioValue = [];
    var portfolioNames = [];
        var stockName = $(this).text();
        var quote = $(this).data('title');
//    var stockData = { stockName: quote};
        var stockquote = JSON.stringify(quote);
        $.ajax({
            url: '/buy_stock/',
            type: 'POST',
            dataType: 'html',
            data: stockquote,
            success: function (response) {
                console.log(response);
            },
            error: function (response) {
                console.log(response)
            }
        }).complete(function () {
            $.ajax({
                url: '/personal_pie_info/',
                type: 'GET',
                dataType: 'json',

                success: function (stock_response) {
                    console.log(stock_response);
                    totalValue =0;
                    for (var key in stock_response) {
                        var value = stock_response[key];
                        console.log(key);
                        console.log(value);
                        portfolioNames.push(key);
                        portfolioValue.push(value);
                        totalValue += value;


                    }

                },
                error: function (error) {
                    console.log(error);
                }
            });

        });
    });

    $('.testBtn').on('click', function () {
//                        Create custom pie graph for each portfolio
        console.log(totalValue);
        // Build the chart
        $('#pieChartPers').highcharts({
            chart: {
                plotBackgroundColor: null,
                plotBorderWidth: null,
                plotShadow: false
            },
            title: {
                text: 'Your Personal Portfolio'
            },
            "subtitle": {
                "text": "Current Value $"+ Number((totalValue).toFixed(2)).toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",")},
            tooltip: {
                pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
            },
            plotOptions: {
               series: {
                animation: {
                    duration: 2000,
                    easing: 'easeOutExpo'
                }
            },
                pie: {
                    allowPointSelect: true,
                    cursor: 'pointer',
                    dataLabels: {
                        enabled: false,
                        format: '<b>{point.name}</b>: {point.percentage:.1f} %',
                        style: {
                            color: (Highcharts.theme && Highcharts.theme.contrastTextColor) || 'black'
                        },
                        connectorColor: 'silver'

                    },
                    showInLegend: true

                }
            },
            series: [
                {
                    type: "pie",
                    name: 'Stocks',
                    data: (function () {
                        // generate an array of random data
                        var data = [],
                            i;

                        for (i = 0; i < portfolioNames.length; i++) {
                            console.log(portfolioNames[i]);
                            data.push([
                                portfolioNames[i], portfolioValue[i]
                            ]);
                        }
                        return data;
                    }())
                }
            ]
        });


    });
});

//.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",")