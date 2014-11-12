from advisor.models import Investor

__author__ = 'Travis'
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper


class EmailUserCreationForm(UserCreationForm):
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    first_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    housing = forms.IntegerField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Monthly Housing Costs'}))
    income = forms.IntegerField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Income amount'}))
    age = forms.IntegerField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Age'}))
    zipcode = forms.IntegerField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Zipcode'}))
    other_costs = forms.FloatField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Other Major Monthly Costs: Debt, etc'}))

    class Meta:
        model = Investor
        fields = ("username", "email", "password1", "password2", "first_name", "last_name", 'income', 'housing', 'age',
                  'zipcode', 'other_costs')

    def __init__(self, *args, **kwargs):
        super(EmailUserCreationForm, self).__init__(*args, **kwargs)

        for fieldname in ['password2']:
            self.fields[fieldname].help_text = None

    def clean_username(self):
            # Since User.username is unique, this check is redundant,
            # but it sets a nicer error message than the ORM. See #13147.
            username = self.cleaned_data["username"]
            try:
                Investor.objects.get(username=username)
            except Investor.DoesNotExist:
                return username
            raise forms.ValidationError(
                self.error_messages['duplicate_username'],
                code='duplicate_username',)


class RiskProfileForm(forms.Form):
    choices = ((3, "Strongly Agree"), (2, "Agree"), (1, "Disagree"), (0, "Strongly Disagree"),)
    timeline = ((3, "More than 4 years"), (2, "2 to 4 years"), (1, "6 months to 2 years"), (0, "Less than 1 year"),)
    negative_questions = ((0, "Strongly Agree"), (1, "Agree"), (2, "Disagree"), (3, "Strongly Disagree"),)
    negative_answers = ((0, "Sell immediately"),
                        (1, "Look to sell shortly"), (3, "Buy the dip"), (2, "Leave my positions alone"),)
    yes_no = ((-3, "YES"), (3, "NO"))
    pos_yes_no = ((3, "YES"), (-3, "NO"))


    One = forms.TypedChoiceField(choices=choices, coerce=int, widget=forms.RadioSelect,
                                 label="I take a long term view on my investments.")
    Two = forms.TypedChoiceField(choices=choices, coerce=int, widget=forms.RadioSelect,
                                 label="I am willing to accept that, once the investment is placed it will fluctuate. ")
    Three = forms.TypedChoiceField(choices=timeline, coerce=int, widget=forms.RadioSelect,
                                   label="I accept that investments can fall in value and take time to recover. "
                                         "However, I would expect these losses to be recovered within:")
    Four = forms.TypedChoiceField(choices=choices, coerce=int, widget=forms.RadioSelect,
                                  label="My current income and assets are very stable and I am "
                                        "currently ready to invest")
    Five = forms.TypedChoiceField(choices=choices, coerce=int, widget=forms.RadioSelect,
                                  label="The stock market doesnt scare me")
    Six = forms.TypedChoiceField(choices=choices, coerce=int, widget=forms.RadioSelect,
                                 label="I am looking for high investment growth. I am willing to accept the possibility"
                                       " of greater losses to achieve this")
    Seven = forms.TypedChoiceField(choices=choices, coerce=int, widget=forms.RadioSelect,
                                   label="I would prefer small certain gains to large uncertain ones")
    Eight = forms.TypedChoiceField(choices=negative_questions, coerce=int, widget=forms.RadioSelect,
                                   label="To obtain above-average returns on my Investments, I am willing to "
                                         "accept above-average risk.")
    Nine = forms.TypedChoiceField(choices=choices, coerce=int, widget=forms.RadioSelect,
                                  label="If my investments lose money over the course of a year, I can easily "
                                        "resist the temptation to sell them.")
    Ten = forms.TypedChoiceField(choices=choices, coerce=int, widget=forms.RadioSelect,
                                 label="I know quite a bit about economic issues and personal investing.")
    Eleven = forms.TypedChoiceField(choices=negative_answers, coerce=int, widget=forms.RadioSelect,
                                    label="If your portfolio lost more than 40% of its value in less than "
                                          "six months, what would you do?")
    Twelve = forms.TypedChoiceField(choices=choices, coerce=int, widget=forms.RadioSelect,
                                    label="I give equal weight to losses and gains")
    Thirteen = forms.TypedChoiceField(choices=yes_no, coerce=int, widget=forms.RadioSelect,
                                      label="Do you need to draw a large amount of money out your portfolio within the "
                                            "next ten years")
    Fourteen = forms.TypedChoiceField(choices=pos_yes_no, coerce=int, widget=forms.RadioSelect,
                                      label="Do you believe that interest rates relate to the performance of investments")
    Fifteen = forms.TypedChoiceField(choices=pos_yes_no, coerce=int, widget=forms.RadioSelect,
                                     label="If one investment had expected returns of 20% but could easily "
                                           "have returns of -20%, would you invest in that?")
    Sixteen = forms.TypedChoiceField(choices=choices, coerce=int, widget=forms.RadioSelect,
                                     label="I would prefer to invest in a well diversified portfolio that spreads"
                                           " my investment across the major asset classes and understand that "
                                           "this may reduce the potential returns although should help to lower "
                                           "the risk profile:")
    helper = FormHelper()


class StockLookUpForm(forms.Form):
    ticker = forms.CharField(max_length=5, widget=forms.TextInput(attrs={'placeholder': 'Ticker Symbol:AAPL, etc'}))



