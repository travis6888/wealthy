import numpy

__author__ = 'Travis'


def demo_age_calc(age):
    percent_month = (float(4000) * .60)
    investment_month = (float(4000) - float(percent_month))
    inv_return = numpy.fv((.058 / 12), ((65 - (int(age))) * 12), -(int(investment_month)), -investment_month)
    investment_return = '{:20,.2f}'.format(float(inv_return))
    vistior_age = {'investment': investment_month, 'age': age, 'return': investment_return,
                   "percent_mon": percent_month}
    return vistior_age


def find_invest_month_calc(investor, monies):
    percent_month = (float(monies) * .60)
    investment_month = (float(monies) - float(percent_month))
    investor.monthly_investment = investment_month
    investor.save()
    investment_clean = '{:20,.2f}'.format(investment_month)
    investing = {'invest': investment_clean}
    return investing


def input_income_calc(investor, income_input):
    taxes = float(income_input) * .06
    after_taxes = float(income_input) - float(taxes)
    investor.after_tax = float(after_taxes)
    print_tax = '{:20,.2f}'.format(after_taxes)
    json_tax = {'after_tax': print_tax}
    return json_tax