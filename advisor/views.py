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
from advisor.models import Investor, Stocks
from wealthy import settings
import ystockquote
import finance
import numpy.lib.financial
from yahoo import *


# @csrf_exempt
def home(request):
    return render(request, 'home.html')


def homeowner(request):
    return render(request, 'homeowner.html')


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
            print picked
            return redirect("boot")

    else:
        form = RiskProfileForm()

    return render(request, 'risk_profile.html', {'form': form})


@csrf_exempt
def stock_lookup(request):
    if request.method == "POST":
        data = json.loads(request.body)
        print data
        # form = StockLookUpForm(request.POST)
        # if form.is_valid():
        # symbol = form.cleaned_data['one']
        string = data['names']
        stock_list1 = []
        for name in string:
            stock_price = ystockquote.get_price(str(name))


            print stock_price
            stock_info = {'stock_price': stock_price}
            stock_list1.append(stock_info)


        data = {'stock_list1': stock_list1}
        return HttpResponse(json.dumps(data), content_type='application/json')
        # return render_to_response('stock_lookup.html', stock_info,
        # context_instance=RequestContext(request))


@csrf_exempt
@login_required()
def mortgage_percentage(request):
    investor = Investor.objects.get(id=request.user.id)
    if request.method == "POST":
        data = json.loads(request.body)
        print data
        income2 = investor.income
        print income2
        rent = data['data']
        desposible_monthly = (float(income2) / 12) - float(rent)
        print desposible_monthly
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
        print rent
        percentage = '{:20,.2f}'.format(float(rent) / (float(after_tax) / 12))

        print after_tax
        print percentage
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
        print income_input
        if int(income_input) >= 200001:
            taxes = float(income_input) * .26
            after_taxes = float(income_input) - float(taxes)
            investor.after_tax = int(after_taxes)
            print_tax = '{:20,.2f}'.format(after_taxes)
            json_tax = {'after_tax': print_tax}
            investor.save()
            return HttpResponse(json.dumps(json_tax), content_type='application/json')
        elif 120000 <= int(income_input) <= 200000:
            taxes = float(income_input) * .18
            print taxes
            after_taxes = (float(income_input) - float(taxes))
            investor.after_tax = int(after_taxes)
            print_tax = '{:20,.2f}'.format(after_taxes)
            json_tax = {'after_tax': print_tax}
            print after_taxes
            investor.save()
            return HttpResponse(json.dumps(json_tax), content_type='application/json')
        elif 60000 <= int(income_input) <= 119999:
            taxes = float(income_input) * .10
            after_taxes = float(income_input) - float(taxes)
            investor.after_tax = int(after_taxes)
            print_tax = '{:20,.2f}'.format(after_taxes)
            json_tax = {'after_tax': print_tax}
            print "f"
            investor.save()
            return HttpResponse(json.dumps(json_tax), content_type='application/json')
        elif 20000 < int(income_input) <= 59999:
            taxes = float(income_input) * .06
            after_taxes = float(income_input) - float(taxes)
            investor.after_tax = float(after_taxes)
            print_tax = '{:20,.2f}'.format(after_taxes)
            json_tax = {'after_tax': print_tax}
            print "g"
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
        if int(age) > 65:
            percent_month = (float(4000) * .60)
            investment_month = (float(4000) - float(percent_month))
            inv_return = numpy.fv((.058 / 12), ((65 - (int(age))) * 12), -(int(investment_month)), -investment_month)
            investment_return = '{:20,.2f}'.format(float(inv_return))
            vistior_age = {'investment': investment_month, 'age': age, 'return': investment_return,
                           "percent_mon": percent_month}
            print investment_month
            return HttpResponse(json.dumps(vistior_age), content_type='application/json')
        elif 45 < int(age) <= 64:
            percent_month = (float(4000) * .70)
            investment_month = (float(4000) - float(percent_month))
            inv_return = numpy.fv((.058 / 12), ((65 - (int(age))) * 12), -(int(investment_month)), -investment_month)
            investment_return = '{:20,.2f}'.format(float(inv_return))
            vistior_age = {'investment': investment_month, 'age': age, 'return': investment_return,
                           "percent_mon": percent_month}
            print investment_month
            return HttpResponse(json.dumps(vistior_age), content_type='application/json')
        elif 35 < int(age) <= 44:
            percent_month = (float(4000) * .80)
            investment_month = (float(4000) - float(percent_month))
            inv_return = numpy.fv((.058 / 12), ((65 - (int(age))) * 12), -(int(investment_month)), -investment_month)
            investment_return = '{:20,.2f}'.format(float(inv_return))
            vistior_age = {'investment': investment_month, 'age': age, 'return': investment_return,
                           "percent_mon": percent_month}
            print investment_month
            return HttpResponse(json.dumps(vistior_age), content_type='application/json')
        elif 14 < int(age) <= 34:
            percent_month = (float(4000) * .85)
            investment_month = (float(4000) - float(percent_month))
            inv_return = numpy.fv((.058 / 12), ((65 - (int(age))) * 12), -(int(investment_month)), -investment_month)
            investment_return = '{:20,.2f}'.format(float(inv_return))
            vistior_age = {'investment': investment_month, 'age': age, 'return': investment_return,
                           "percent_mon": percent_month}
            print investment_month
            return HttpResponse(json.dumps(vistior_age), content_type='application/json')


@csrf_exempt
@login_required()
def find_investment_monthly(request):
    investor = Investor.objects.get(id=request.user.id)
    if request.method == "GET":
        age = investor.age
        monies = investor.disposible_monthly
        print age
        print monies

        if int(age) >= 65:

            percent_month = (float(monies) * .60)
            investment_month = (float(monies) - float(percent_month))
            investor.monthly_investment = investment_month
            investor.save()
            investment_clean = '{:20,.2f}'.format(investment_month)
            investing = {'invest': investment_clean}
            return HttpResponse(json.dumps(investing), content_type='application/json')
        elif 45 <= int(age) <= 64:
            percent_month = (float(monies) * .70)
            investment_month = (float(monies) - float(percent_month))
            investor.monthly_investment = investment_month
            investor.save()
            investment_clean = '{:20,.2f}'.format(investment_month)

            investing = {'invest': investment_clean}
            return HttpResponse(json.dumps(investing), content_type='application/json')
        elif 35 <= int(age) <= 44:
            percent_month = (float(monies) * .75)

            investment_month = (float(monies) - float(percent_month))
            investor.monthly_investment = investment_month
            investor.save()
            investment_clean = '{:20,.2f}'.format(investment_month)

            investing = {'invest': investment_clean}
            return HttpResponse(json.dumps(investing), content_type='application/json')
        else:
            percent_month = (float(monies) * .80)
            investment_month = (float(monies) - float(percent_month))
            investor.monthly_investment = investment_month
            investor.save()
            investment_clean = '{:20,.2f}'.format(investment_month)
            investing = {'invest': investment_clean}
            return HttpResponse(json.dumps(investing), content_type='application/json')


# @csrf_exempt
# @login_required()
# def calculate(request):
# investor = Investor.objects.get(id=request.user.id)
#     if request.method == "POST":

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
        print investment
        print risky
        if int(risky) > 40:
            inv_return = numpy.fv((.097 / 12), ((65 - (int(age))) * 12), -(int(investment)), -investment)
            investment_return = '{:20,.2f}'.format(float(inv_return))
            data2 = {'stocksp': {'stock1p': 25, 'stock2p': 25, 'stock3p': 20, 'stock4p': 20, 'stock5p': 10},
                     'stocksn': {'stock1n': "VOO", 'stock2n': "VWO", 'stock3n': 'VO', 'stock4n': 'VTWO', 'stock5n': 'VTI'},
                    'portfolio': 'Super Aggressive',
                    'expected': 9.7,
                    'return': investment_return}
            return HttpResponse(json.dumps(data2), content_type='application/json')

        elif 32 <= int(risky) <= 40:
            inv_return = numpy.fv((.083 / 12), ((65 - (int(age))) * 12), -(int(investment)), -investment)
            investment_return = '{:20,.2f}'.format(float(inv_return))
            data2 = {'stocksp': {'stock1p': 40, 'stock2p': 20, 'stock3p': 20, 'stock4p': 15, 'stock5p': 5 },
                     'stocksn': {'stock1n': "VOO", 'stock2n': "VWO", 'stock3n': 'VTI', 'stock4n': 'VONE', 'stock5n': 'VTWO'},
                    'portfolio': 'Aggressive',
                    'expected': 8.3,
                    'return': investment_return}
            return HttpResponse(json.dumps(data2), content_type='application/json')
        elif 24 <= int(risky) <= 31:
            inv_return = numpy.fv((.067 / 12), ((65 - (int(age))) * 12), -(int(investment)), -investment)
            investment_return = '{:20,.2f}'.format(float(inv_return))
            data2 = {'stocksp': {'stock1p': 30, 'stock2p': 30, 'stock3p': 20, 'stock4p': 15, 'stock5p': 15},
                 'stocksn': {'stock1n': "VOO", 'stock2n': "VCIT", 'stock3n': 'VGK', 'stock4n': 'VTI', 'stock5n': 'VYM'},
                'portfolio': 'Moderate',
                'expected': 6.7,
                'return': investment_return}
            return HttpResponse(json.dumps(data2), content_type='application/json')
        elif 12 <= int(risky) <= 23:
            inv_return = numpy.fv((.058 / 12), ((65 - (int(age))) * 12), -(int(investment)), -investment)
            investment_return = '{:20,.2f}'.format(float(inv_return))
            data2 = {'stocksp': {'stock1p': 30, 'stock2p': 30, 'stock3p': 20, 'stock4p': 10, 'stock5p': 10},
                     'stocksn': {'stock1n': "VCIT", 'stock2n': "VOO", 'stock3n': 'VGLT', 'stock4n': 'VNQ', 'stock5n': 'VYM'},
                    'portfolio': 'Conservative',
                    'expected': 5.8,
                    'return': investment_return}
            return HttpResponse(json.dumps(data2), content_type='application/json')
        else:
            inv_return = numpy.fv((.04 / 12), ((65 - (int(age))) * 12), -(int(investment)), -investment)
            investment_return = '{:20,.2f}'.format(float(inv_return))
            data2 = {'stocksp': {'stock1p': 40, 'stock2p': 30, 'stock3p': 20, 'stock4p': 10, 'stock5p': 10},
                     'stocksn': {'stock1n': "VCIT", 'stock2n': "VGLT", 'stock3n': 'VOO', 'stock4n': 'VNQ', 'stock5n': 'VYM'},
                    'portfolio': 'Super Conservative',
                    'expected': 4.0,
                    'return': investment_return}
            return HttpResponse(json.dumps(data2), content_type='application/json')


def boot(request):
    return render(request, 'boot4.html')

@csrf_exempt
def stock_info(request):
    if request.method == "POST":
        data = json.loads(request.body)
        print data
        names = data['names']
        print names
        stock_list = []
        for name in names:
            stock = Stocks.objects.get(name=name)
            stock_description = {
                'name': stock.name,
                'info': stock.info
            }
            stock_list.append(stock_description)
        data = {'stock_list': stock_list}
        print stock_list
        return HttpResponse(json.dumps(data), content_type='application/json')
