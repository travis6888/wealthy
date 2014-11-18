import json
import user
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.core import serializers
from django.core.mail import EmailMultiAlternatives
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, render_to_response

# Create your views here.
from django.template import RequestContext
from django.utils import formats
from django.views.decorators.csrf import csrf_exempt
from requests import auth
from advisor.forms import EmailUserCreationForm, RiskProfileForm, StockLookUpForm
from advisor.models import Investor, Stocks, Portfolio, Investment
from wealthy import settings
import ystockquote
import finance
import numpy.lib.financial
from yahoo import *


# @csrf_exempt
from wealthy.utils import demo_age_calc, find_invest_month_calc, input_income_calc, portfolio_return_calc







@login_required
def profile(request):
    return render(request, 'profile.html', {})


def register(request):
    if request.method == 'POST':
        form = EmailUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, "Thanks for registering. You are now logged in.")
            new_user = authenticate(username=request.POST['username'],
                                    password=request.POST['password1'])
            login(request, new_user)
            return HttpResponseRedirect(reverse("boot"))

    else:
        form = EmailUserCreationForm()

    return render(request, "registration/register.html", {
        'form': form,
    })


@login_required
def edit_profile(request, user_id):
    profile_user = Investor.objects.get(id=user_id)
    if request.user == profile_user:
        if request.method == 'POST':
            form = EmailUserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect(reverse('boot'))
        else:
            form = EmailUserCreationForm()
        return render(request, "registration/register.html",
                      {'form': form, "user": profile_user})

    else:
        return redirect("boot")


@login_required()
def risk_profile(request):
    investor = Investor.objects.get(id=request.user.id)
    if request.method == 'POST':
        form = RiskProfileForm(request.POST)
        if form.is_valid():
            picked = form.cleaned_data['One']
            picked += form.cleaned_data['Two']
            picked += form.cleaned_data['Three']
            picked += form.cleaned_data['Four']
            picked += form.cleaned_data['Five']
            picked += form.cleaned_data['Six']
            picked += form.cleaned_data['Seven']
            picked += form.cleaned_data['Eight']
            picked += form.cleaned_data['Nine']
            picked += form.cleaned_data['Ten']
            picked += form.cleaned_data['Eleven']
            picked += form.cleaned_data['Twelve']
            picked += form.cleaned_data['Thirteen']
            picked += form.cleaned_data['Fourteen']
            picked += form.cleaned_data['Fifteen']
            picked += form.cleaned_data['Sixteen']
            investor.risk_score = int(picked)
            investor.save()
            return redirect("boot")

    else:
        form = RiskProfileForm()

    return render(request, 'risk_profile.html', {'form': form})


@csrf_exempt
def stock_lookup(request):
    if request.method == "POST":
        data = json.loads(request.body)
        string = data['names']
        stock_list1 = []
        for name in string:
            stock_price = ystockquote.get_price(str(name))
            stock_info = {'stock_price': stock_price}
            stock_list1.append(stock_info)

        data = {'stock_list1': stock_list1}
        return HttpResponse(json.dumps(data), content_type='application/json')


@csrf_exempt
@login_required()
def mortgage_percentage(request):
    investor = Investor.objects.get(id=request.user.id)
    if request.method == "POST":
        data = json.loads(request.body)
        income2 = investor.income
        rent = data['data']
        desposible_monthly = (float(income2) / 12) - float(rent)
        investor.housing = rent
        investor.save()
        desposible_monthly = {'desposible_income': desposible_monthly}
        return HttpResponse(json.dumps(desposible_monthly), content_type='application/json')


@login_required()
@csrf_exempt
def rent_to_median(request):
    investor = Investor.objects.get(id=request.user.id)
    if request.method == "GET":
        rent = investor.housing
        after_tax = investor.after_tax
        percentage = '{:20,.2f}'.format(float(rent) / (float(after_tax) / 12))
        monthly = (float(after_tax) / 12) - float(rent)
        investor.disposible_monthly = int(monthly)
        investor.save()
        clean_monthly = '{:20,.2f}'.format(monthly)
        percentage_return = {'percentage_housing': percentage, 'disposible': clean_monthly}
        return HttpResponse(json.dumps(percentage_return), content_type='application/json')


@csrf_exempt
@login_required()
def input_income(request):
    investor = Investor.objects.get(id=request.user.id)
    if request.method == "GET":
        income_input = investor.income
        if int(income_input) >= 200001:
            taxes = float(income_input) * .33
            json_tax = input_income_calc(investor, income_input, taxes)

            return HttpResponse(json.dumps(json_tax), content_type='application/json')
        elif 120000 <= int(income_input) <= 200000:
            taxes = float(income_input) * .26
            json_tax = input_income_calc(investor, income_input, taxes)
            investor.save()
            return HttpResponse(json.dumps(json_tax), content_type='application/json')
        elif 60000 <= int(income_input) <= 119999:
            taxes = float(income_input) * .17
            json_tax = input_income_calc(investor, income_input, taxes)
            investor.save()
            return HttpResponse(json.dumps(json_tax), content_type='application/json')
        elif 20000 < int(income_input) <= 59999:
            taxes = float(income_input) * .10
            json_tax = input_income_calc(investor, income_input, taxes)
            investor.save()
            return HttpResponse(json.dumps(json_tax), content_type='application/json')
        else:

            investor.after_tax = income_input
            investor.save()
            redirect('home')
            return HttpResponse(json.dumps(income_input), content_type='application/json')


@csrf_exempt
def demo_age(request):
    if request.method == "POST":
        data = json.loads(request.body)
        age = data['data']
        if int(age) >= 65:
            visitor_age = demo_age_calc(age)
            return HttpResponse(json.dumps(visitor_age), content_type='application/json')
        elif 45 <= int(age) <= 64:
            visitor_age = demo_age_calc(age)
            return HttpResponse(json.dumps(visitor_age), content_type='application/json')
        elif 35 <= int(age) <= 44:
            visitor_age = demo_age_calc(age)
            return HttpResponse(json.dumps(visitor_age), content_type='application/json')
        elif 0 < int(age) <= 34:
            visitor_age = demo_age_calc(age)
            return HttpResponse(json.dumps(visitor_age), content_type='application/json')


@csrf_exempt
@login_required()
def find_investment_monthly(request):
    investor = Investor.objects.get(id=request.user.id)
    if request.method == "GET":
        age = investor.age
        monies = investor.disposible_monthly
        if int(age) >= 65:
            percent_month = (float(monies) * .40)
            investing = find_invest_month_calc(investor, monies, percent_month)
            return HttpResponse(json.dumps(investing), content_type='application/json')
        elif 45 <= int(age) <= 64:
            percent_month = (float(monies) * .55)
            investing = find_invest_month_calc(investor, monies, percent_month)
            return HttpResponse(json.dumps(investing), content_type='application/json')
        elif 35 <= int(age) <= 44:
            percent_month = (float(monies) * .65)
            investing = find_invest_month_calc(investor, monies, percent_month)
            return HttpResponse(json.dumps(investing), content_type='application/json')
        else:
            percent_month = (float(monies) * .75)
            investing = find_invest_month_calc(investor, monies, percent_month)
            return HttpResponse(json.dumps(investing), content_type='application/json')


def find_investment(request):
    investor = Investor.objects.get(id=request.user.id)
    if request.method == "POST":
        monthly = investor.disposible_monthly
        data = json.loads(request.body)


@csrf_exempt
def find_portfolio(request):
    investor = Investor.objects.get(id=request.user.id)
    if request.method == "GET":
        risky = investor.risk_score
        monthly = investor.disposible_monthly
        age = investor.age
        investment = investor.monthly_investment
        if int(risky) > 40:
            risk_portfolio = "Super Aggressive"
            data2 = portfolio_return_calc(age, investment, risk_portfolio,)
            return HttpResponse(json.dumps(data2), content_type='application/json')
        elif 32 <= int(risky) <= 40:
            risk_portfolio = "Aggressive"
            data2 = portfolio_return_calc(age, investment, risk_portfolio,)
            return HttpResponse(json.dumps(data2), content_type='application/json')
        elif 24 <= int(risky) <= 31:
            risk_portfolio = "Moderate"
            data2 = portfolio_return_calc(age, investment, risk_portfolio,)
            return HttpResponse(json.dumps(data2), content_type='application/json')
        elif 12 <= int(risky) <= 23:
            risk_portfolio = "Conservative"
            data2 = portfolio_return_calc(age, investment, risk_portfolio,)
            return HttpResponse(json.dumps(data2), content_type='application/json')
        else:
            risk_portfolio = "Super Conservative"
            data2 = portfolio_return_calc(age, investment, risk_portfolio,)
            return HttpResponse(json.dumps(data2), content_type='application/json')


def boot(request):
    investor = Investor.objects.get(id=request.user.id)
    investor_data ={'zip': investor.zipcode, 'housing': investor.housing}
    return render(request, 'boot4.html', investor_data)


def home(request):
    return render(request, 'boot4.html')


def dashboard(request):
    stock_list = {'stocks':{}}
    investor = Investor.objects.get(id=request.user.id)
    for stock in investor.portfolio.investments.all():
        quote = stock.hidden_symbol
        price = ystockquote.get_price(str(quote))
        stock_list['stocks'][quote] = price

    return render(request, 'dashboard.html', stock_list)

@csrf_exempt
def price_lookup(request):
    stock_list = {'stocks':{}}
    investor = Investor.objects.get(id=request.user.id)
    for stock in investor.portfolio.investments.all():
        quote = stock.hidden_symbol
        price = ystockquote.get_price(str(quote))
        stock_list['stocks'][quote] = price


    return HttpResponse(json.dumps(stock_list), content_type='application/json')