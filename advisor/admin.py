from django.contrib import admin

# Register your models here.
from advisor.models import Investor, Portfolio, Investment, AssetType, Stocks

admin.site.register(Investor)
admin.site.register(Portfolio)
admin.site.register(Investment)
admin.site.register(AssetType)
admin.site.register(Stocks)