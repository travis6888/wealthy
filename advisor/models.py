from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class AssetType(models.Model):
    name = models.CharField(max_length=100)
    sector = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name


class Investment(models.Model):
    name = models.CharField(max_length=100)
    asset_type = models.CharField(max_length=50)
    fees = models.PositiveSmallIntegerField(max_length=10)
    sector = models.CharField(max_length=100)
    country = models.CharField(max_length=70)
    url = models.URLField

    def __unicode__(self):
        return u"{}".format(self.name, self.asset_type, self.fees, self.sector, self.country)


class Portfolio(models.Model):
    assets = models.ManyToManyField(Investment)
    user = models.ForeignKey(User)
