from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class Investor(AbstractUser):
    risk_score = models.FloatField(null=True, default=0)
    income = models.FloatField(null=True, default=0)
    housing = models.FloatField(null=True, default=0)
    disposible_monthly = models.FloatField(null=True, default=0)
    age = models.FloatField(null=True, default=18)
    zipcode = models.FloatField(null=True, default=0, max_length=5)
    after_tax = models.FloatField(null=True, default=0)
    monthly_investment = models.FloatField(null=True, default=0, max_length=20)
    other_costs = models.FloatField(null=True, blank=True, default=0, max_length=20)
    portfolio_name = models.CharField(max_length=25, blank=True, null=True)

    def __unicode__(self):
        return u"{} {}".format(self.username, self.income)


class AssetType(models.Model):
    name = models.CharField(max_length=100)
    sector = models.CharField(max_length=100)
    country = models.CharField(max_length=70)

    def __unicode__(self):
        return u"{}".format(self.name)


class Investment(models.Model):
    name = models.CharField(max_length=100)
    asset_type = models.ForeignKey(AssetType, related_name='investments')
    fees = models.FloatField(max_length=5, default=0)
    url = models.URLField(blank=True, null=True)
    description = models.TextField(max_length=1000, blank=True, null=True)
    hidden_symbol = models.TextField(max_length=5, blank=True, null=True)

    def __unicode__(self):
        return u"{}".format(self.name, self.asset_type)


class Portfolio(models.Model):
    name = models.CharField(max_length=100)
    investments = models.ManyToManyField(Investment, related_name='portfolios')
    investor = models.OneToOneField(Investor, related_name="portfolio")
    expected_return = models.FloatField(max_length=5, default=0, blank=True, null=True)

    def __unicode__(self):
        return u"{}".format(self.name)


class Stocks(models.Model):
    name = models.CharField(max_length=10)
    info = models.TextField(max_length=3000)

    def __unicode__(self):
        return u"{}".format(self.name)