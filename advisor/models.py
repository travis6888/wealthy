from django.contrib.auth.models import User, AbstractUser
from django.db import models

# Create your models here.

class Investor(AbstractUser):
    risk_score = models.IntegerField(null=True)
    income = models.IntegerField(null=True)

    def __unicode__(self):
        return self.risk_score


class AssetType(models.Model):
    name = models.CharField(max_length=100)
    sector = models.CharField(max_length=100)
    country = models.CharField(max_length=70)

    def __unicode__(self):
        return self.name


class Investment(models.Model):
    name = models.CharField(max_length=100)
    asset_type = models.ForeignKey(AssetType, related_name='investments')
    fees = models.PositiveSmallIntegerField(max_length=10)
    url = models.URLField()

    def __unicode__(self):
        return u"{}".format(self.name, self.asset_type, self.fees, self.sector, self.country)


class Portfolio(models.Model):
    name = models.CharField(max_length=100)
    investments = models.ManyToManyField(Investment, related_name='portfolios')
    investor = models.ForeignKey(Investor)

    def __unicode__(self):
        return self.name
