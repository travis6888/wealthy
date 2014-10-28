import numpy
from advisor.models import Portfolio, Investment

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


def portfolio_return_calc(age, investment, risk_portfolio ):
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
                     'stocksn': {'stock1n': stock_name[0], 'stock2n': stock_name[1], 'stock3n': stock_name[2], 'stock4n':stock_name[3], 'stock5n': stock_name[4]},
                    'portfolio': portfolio_attr[0],
                    'expected': portfolio_attr[1],
                    'return': investment_return, 'stock_list': stock_info_list}
    return data2