
from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

from django.contrib import admin
import advisor

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'advisor.views.home', name='home'),
    url(r'^home/$', 'advisor.views.home', name='home'),
    url(r'^register/$', 'advisor.views.register', name='register'),
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout',  {'next_page': '/home/'}, name="logout"),
    # url(r'^profile/$', 'advisor.views.profile', name='profile'),
    url(r'^risk_profile/$', 'advisor.views.risk_profile', name='risk_profile'),
    url(r'^profile/$', 'advisor.views.profile', name='profile'),
    url(r'^stock_lookup/$', 'advisor.views.stock_lookup', name='stock_lookup'),
    url(r'^mortgage_percentage/(?P<user_id>\d+)$', 'advisor.views.mortgage_percentage', name='mortgage_percentage'),
    url(r'^income/$', 'advisor.views.input_income', name='income'),
    url(r'^rent_to_median/$', 'advisor.views.rent_to_median', name='rent_to_median'),
    url(r'^find_investment_monthly/$', 'advisor.views.find_investment_monthly', name='find_investment_monthly'),

    url(r'^demo_age/$', 'advisor.views.demo_age', name='demo_age'),

    url(r'^boot/$', 'advisor.views.boot', name='boot'),
    url(r'^find_portfolio/$', 'advisor.views.find_portfolio', name='find_portfolio'),


    url(r'^password_reset/$', 'django.contrib.auth.views.password_reset', name='password_reset'),
    url(r'^password_reset/done/$', 'django.contrib.auth.views.password_reset_done', name='password_reset_done'),
    # Support old style base36 password reset links; remove in Django 1.7
    url(r'^reset/(?P<uidb36>[0-9A-Za-z]{1,13})-(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        'django.contrib.auth.views.password_reset_confirm_uidb36'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        'django.contrib.auth.views.password_reset_confirm',
        name='password_reset_confirm'),
    url(r'^reset/done/$', 'django.contrib.auth.views.password_reset_complete', name='password_reset_complete'),
    url(r'^admin/', include(admin.site.urls)),
)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)