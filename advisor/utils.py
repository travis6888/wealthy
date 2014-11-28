from decimal import Decimal
import decimal
import math
import numpy
import ystockquote
from advisor.models import Portfolio, Investment, PersonalStockPortfolio

__author__ = 'Travis'


def demo_age_calc(age):
    percent_month = (float(4000) * .70)
    investment_month = (float(4000) - float(percent_month))
    inv_return = numpy.fv((.058 / 12), ((65 - (int(age))) * 12), -(int(investment_month)), -investment_month)
    investment_return = '{:20,.2f}'.format(float(inv_return))
    vistior_age = {'investment': investment_month, 'age': age, 'return': investment_return,
                   "percent_mon": percent_month}
    return vistior_age


def find_invest_month_calc(investor, monies, percent_month):
    investment_month = (float(monies) - float(percent_month))
    investor.monthly_investment = investment_month
    investor.save()
    investment_clean = '{:20,.2f}'.format(investment_month)
    investing = {'invest': investment_clean}
    return investing


def input_income_calc(investor, income_input, taxes):
    after_taxes = float(income_input) - float(taxes)
    investor.after_tax = float(after_taxes)
    print_tax = '{:20,.2f}'.format(after_taxes)
    json_tax = {'after_tax': print_tax}
    investor.save()
    return json_tax


def portfolio_return_calc(age, investment, risk_portfolio, investor):
    portfolio_attr = []
    portfolio_list = Portfolio.objects.filter(name=risk_portfolio)
    stock_list = Investment.objects.filter(portfolios__name=risk_portfolio)
    stock_name = []
    stock_info_list = []
    for stock in stock_list:
        stock_name.append(stock.name)
        stock_description = {
            'name': stock.name,
            'info': stock.description}
        stock_info_list.append(stock_description)
    for portfolio in portfolio_list:
        portfolio_attr.append(portfolio.name)
        portfolio_attr.append(portfolio.expected_return)
    inv_return = numpy.fv((float(portfolio_attr[1]) / 12), ((65 - (int(age))) * 12), -(int(investment)), -investment)
    investment_return = '{:20,.2f}'.format(float(inv_return))
    data2 = {'stocksp': {'stock1p': 25, 'stock2p': 25, 'stock3p': 20, 'stock4p': 20, 'stock5p': 10},
             'stocksn': {'stock1n': stock_name[0], 'stock2n': stock_name[1], 'stock3n': stock_name[2],
                         'stock4n': stock_name[3], 'stock5n': stock_name[4]},
             'portfolio': portfolio_attr[0],
             'expected': portfolio_attr[1],
             'return': investment_return, 'stock_list': stock_info_list}
    investor.portfolio_name = risk_portfolio
    investor.save()
    return data2


def get_stock_cost(data, number_shares, items):
    price = ystockquote.get_price(str(data))
    cost = float(price) * float(number_shares)
    real_cost = decimal.Decimal(cost)
    items.cost += real_cost
    items.save()
    return real_cost


def get_stock_value(data, number_shares):
    price = ystockquote.get_price(str(data))
    cost = float(price) * float(number_shares)
    real_cost = decimal.Decimal(cost)
    return cost


def get_portfolio_value(items):
    stock_portfolio_info = {}
    portfolio_value = 0
    stock_portfolio_info[items.stock_one_name] = float(items.stock_one_shares)
    stock_portfolio_info[items.stock_two_name] = float(items.stock_two_shares)
    stock_portfolio_info[items.stock_three_name] = float(items.stock_three_shares)
    stock_portfolio_info[items.stock_four_name] = float(items.stock_four_shares)
    stock_portfolio_info[items.stock_five_name] = float(items.stock_five_shares)
    for i in stock_portfolio_info.items():
        data = i[0]
        number_shares = i[1]
        cost = get_stock_value(data, number_shares)
        portfolio_value += cost
    items.current_value = decimal.Decimal(portfolio_value)
    items.save()
    data = {'stockPort': stock_portfolio_info}
    data2 = {'portValue': float(items.current_value),
            'portCost': float(items.cost)}
    return [data, data2]


def empty_stock_add_shares(data, items, number_shares):
    if items.stock_one_name == str(data):
        items.stock_one_shares += number_shares
        get_stock_cost(data, number_shares, items)
        get_portfolio_value(items)
        items.save()
    elif items.stock_one_name is None:
        items.stock_one_name = str(data)
        items.stock_one_shares += number_shares
        get_stock_cost(data, number_shares, items)
        get_portfolio_value(items)
        items.save()
    elif items.stock_two_name == str(data):
        items.stock_two_shares += number_shares
        get_stock_cost(data, number_shares, items)
        get_portfolio_value(items)
        items.save()
    elif items.stock_two_name is None:
        items.stock_two_name = str(data)
        items.stock_two_shares += number_shares
        get_stock_cost(data, number_shares, items)
        get_portfolio_value(items)
        items.save()
    elif items.stock_three_name == str(data):
        items.stock_three_shares += number_shares
        get_stock_cost(data, number_shares, items)
        get_portfolio_value(items)
        items.save()
    elif items.stock_three_name is None:
        items.stock_three_name = str(data)
        items.stock_three_shares += number_shares
        get_stock_cost(data, number_shares, items)
        get_portfolio_value(items)
        items.save()
    elif items.stock_four_name == str(data):
        items.stock_four_shares += number_shares
        get_stock_cost(data, number_shares, items)
        get_portfolio_value(items)
        items.save()
    elif items.stock_four_name is None:
        items.stock_four_name = str(data)
        items.stock_four_shares += number_shares
        get_stock_cost(data, number_shares, items)
        get_portfolio_value(items)
        items.save()
    elif items.stock_five_name == str(data):
        items.stock_five_shares += number_shares
        get_stock_cost(data, number_shares, items)
        get_portfolio_value(items)
        items.save()
    elif items.stock_five_name is None:
        items.stock_five_name = str(data)
        items.stock_five_shares += number_shares
        get_stock_cost(data, number_shares, items)
        get_portfolio_value(items)
        items.save()
    else:
        pass
    return


def buy_stock_conditionals(data, portfolio, monthly, request):
    price = ystockquote.get_price(str(data))
    number_shares = math.trunc(float(monthly) / float(price))
    if portfolio:
        for items in portfolio:
            empty_stock_add_shares(data, items, number_shares)
    else:
        price = ystockquote.get_price(str(data))
        cost = float(price) * float(number_shares)
        real_cost = decimal.Decimal(cost)
        PersonalStockPortfolio.objects.create(name="primary", owner=request.user, stock_one_name=str(data),
                                              stock_one_shares=number_shares, cost=real_cost)
    data = {data: number_shares}
    return data


def match_stocks(data, portfolio_stocks):
    data_list = {}
    for stock, values in data[0]['stockPort'].iteritems():
        for quote in portfolio_stocks:
            if stock == quote.hidden_symbol:
                value = (float(ystockquote.get_price(stock))*values)
                data_list[quote.name] = value
            else:
                pass
    return data_list









