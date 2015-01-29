from django.db import models

# Create your models here.
from advisor.models import Investor


class Blog(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    meta = models.TextField(max_length=1000, blank=True, null=True)
    content = models.TextField(max_length=12000, blank=True, null=True)
    author = models.ForeignKey(Investor, blank=True, null=True)
