/**
 * Created by Travis on 11/13/14.
 */
$(document).ready(function () {
    var names = [];
    var stocks = {'names': []};
    var totalValue = 0;
    var portfolioValue = [];
    var portfolioNames = [];
    var portCost = [];
    var portValue = [];
    $('.loadPort').on('click', function () {
        var values = [];
        var portfolio = [];
        var expected = [];
//                    Get all the portfolio information after the user has a risk score
        $.ajax({
            url: '/find_portfolio/',
            type: 'GET',
            dataType: 'json',
            beforeSend: function () {
                $('#loadingPort').toggle();
                $('#loadingProgress').toggle();
            },
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
                beforeSend: function () {

                },
                success: function (response) {
                    for (var key in response) {
                        var value = response[key];

                        $('.quotesData').toggle();

                        $('.quotesData').append("<button class='btn btn-default btn-md stocks' data-title=" + value + ">" + key + "</button>")
                    }
                },
                error: function (error) {
                    $('.loadPort').toggle();
                }
            });
        }).complete(function () {
//            grab data from models and do calculations in python in views and utils files
            $.ajax({
                url: '/personal_pie_info/',
                type: 'GET',
                dataType: 'json',
                beforeSend: function () {
//                    $('#loading').toggle();
                },
                success: function (stock_response) {
                    totalValue = 0;
                    for (var key in stock_response[0]) {
                        var value = stock_response[0][key];
                        portfolioNames.push(key);
                        portfolioValue.push(value);
                        totalValue += value;

                    }
                    var currentVal = parseFloat(stock_response[1]['portValue']);
                    var expectedVal = parseFloat((stock_response[1]['portExpect'] - stock_response[1]['portValue']));
                    var gain = (stock_response[1]['portValue'] - stock_response[1]['portCost']);
                    $('#loadingPort').toggle();
                    $('#loadingProgress').toggle();

                    $('#progressChart').highcharts({
                        chart: {
                            type: 'pyramid',
                            marginRight: 100
                        },
                        title: {
                            text: 'Portfolio Progress',
                            x: -50
                        },
                        plotOptions: {
                            series: {
                                dataLabels: {
                                    enabled: true,
                                    format: '<b>{point.name}</b> ({point.y:,.0f})',
                                    color: (Highcharts.theme && Highcharts.theme.contrastTextColor) || 'green',
                                    softConnector: true
                                },
                                showInLegend: true
                            }

                        },
                        legend: {
                            title: {
                                text: 'Portfolio Progress',
                                style: {
                                    fontStyle: 'italic'
                                }
                            },
                            layout: 'vertical',
                            align: 'right',
                            verticalAlign: 'top'
//                        x: -10,
//                        y: 100
                        },
                        series: [
                            {
                                name: 'Expect Portfolio Data',
                                data: [
                                    ['Current Value $', Number((currentVal).toFixed(2))],
                                    ['Expected Value $', Number((expectedVal).toFixed(2))]

                                ]
                            }
                        ]
                    });

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
                            "text": "Current Value $" + Number((totalValue).toFixed(2)).toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",")},
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
                                    // generate an data from their personal portfolio model, for loop because there could be less than five
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
                    portfolioNames.length = 0;
                    portfolioValue.length = 0;
                },
                error: function (error) {
                }
            });
        });
    });


    $('.quotesData').on('click', 'button', function () {
        var totalValue = 0;

        var quote = $(this).data('title');
        var stockquote = JSON.stringify(quote);
//        send specific quote to add to personal portfolio and get cost, value, matching data
        $.ajax({
            url: '/buy_stock/',
            type: 'POST',
            dataType: 'html',
            data: stockquote,
            beforeSend: function () {
                $('.stocks').toggle();

                $('#loadingQuotes').toggle();

            },
            success: function (response) {
            },
            error: function (response) {
            }
        }).complete(function () {
//            Do calculations in python backend to make it clean and easy
            $.ajax({
                url: '/personal_pie_info/',
                type: 'GET',
                dataType: 'json',
                success: function (stock_response) {
                    totalValue = 0;
                    console.log(stock_response);

                    for (var key in stock_response[0]) {
                        var value = stock_response[0][key];
                        portfolioNames.push(key);
                        portfolioValue.push(value);
                        totalValue += value;
                    }
                    for (var key2 in stock_response[1]) {
                        var value2 = stock_response[1][key2];
                        console.log(key2);
                        console.log(value2);
                    }
                    $('.updateBtn').toggle();
                    $('.updateWords').append('<h4>Please update graph</h4>');
                    $('#loadingQuotes').toggle()
                },
                error: function (error) {
                }
            });
        });
    });

    $('.updateBtn').on('click', function () {
        $('.updateBtn').toggle();
        $('.updateWords').toggle();
        $('.quotesData').toggle();
//                        Create custom pie graph for each portfolio from database.
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
                "text": "Current Value $" + Number((totalValue).toFixed(2)).toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",")},
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
                        // generate pie with stocks in database, may not own all five so for loop made sense
                        var data = [],
                            i;
                        for (i = 0; i < portfolioNames.length; i++) {
                            data.push([
                                portfolioNames[i], portfolioValue[i]
                            ]);
                        }
                        return data;
                    }())
                }
            ]
        });
        $('#progressChart').highcharts({
                        chart: {
                            type: 'pyramid',
                            marginRight: 100
                        },
                        title: {
                            text: 'Portfolio Progress',
                            x: -50
                        },
                        plotOptions: {
                            series: {
                                dataLabels: {
                                    enabled: true,
                                    format: '<b>{point.name}</b> ({point.y:,.0f})',
                                    color: (Highcharts.theme && Highcharts.theme.contrastTextColor) || 'green',
                                    softConnector: true
                                },
                                showInLegend: true
                            }

                        },
                        legend: {
                            title: {
                                text: 'Portfolio Progress',
                                style: {
                                    fontStyle: 'italic'
                                }
                            },
                            layout: 'vertical',
                            align: 'right',
                            verticalAlign: 'top'
//                        x: -10,
//                        y: 100
                        },
                        series: [
                            {
                                name: 'Expect Portfolio Data',
                                data: [
                                    ['Current Value $', Number((currentVal).toFixed(2))],
                                    ['Expected Value $', Number((expectedVal).toFixed(2))]

                                ]
                            }
                        ]
                    });
    });

    $('.newPort').on('click', function (){
        $.ajax({
                url: '/price_lookup/',
                type: 'GET',
                dataType: 'json',
                beforeSend: function () {

                },
                success: function (response) {
                    console.log(response);
                    for (var key in response) {
                        var value = response[key];

                        $('.quotesData2').toggle();

                        $('.quotesData2').append("<button class='btn btn-default btn-md stocks' data-title=" + value + ">" + key + "</button>")
                    }
                },
                error: function (error) {
//                    $('.loadPort').toggle();
                }
            });
    });
$('.quotesData2').on('click', 'button', function () {
        var totalValue = 0;
        var portfolioValue = [];
        var portfolioNames = [];
        var quote = $(this).data('title');
        var stockquote = JSON.stringify(quote);
//        send specific quote to add to personal portfolio and get cost, value, matching data
        $.ajax({
            url: '/buy_stock/',
            type: 'POST',
            dataType: 'html',
            data: stockquote,
            beforeSend: function () {
                $('.stocks').toggle();

                $('#loadingQuotes').toggle();

            },
            success: function (response) {
            },
            error: function (response) {
            }
        }).complete(function () {
//            Do calculations in python backend to make it clean and easy
            $.ajax({
                url: '/personal_pie_info/',
                type: 'GET',
                dataType: 'json',
                success: function (stock_response) {
                    totalValue = 0;
                    for (var key in stock_response[0]) {
                        var value = stock_response[0][key];

                        portfolioNames.push(key);
                        portfolioValue.push(value);
                        totalValue += value;
                    }
                    for (var key2 in stock_response[1]) {
                        var value2 = stock_response[1][key];
                        console.log(key2);
                        console.log(value2);
                    }
                   window.location.replace("/dashboard/");
                },
                error: function (error) {
                }
            });
        });
    });

});
