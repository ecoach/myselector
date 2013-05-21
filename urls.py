from django.conf.urls.defaults import patterns, include, url

from myselector.views import *
from django.contrib.auth.decorators import login_required

from django.views.generic.simple import redirect_to

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # login / logout
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'myselector/login.html'}),
    url(r'^logout', 'myselector.views.mylogout'),

    # menu items
    url(r'^about/$', About_View.as_view(), name='about'),
    url(r'^tailoring/$', Tailoring_View.as_view(), name='tailoring'),
    url(r'^team/$', Team_View.as_view(), name='team'),
    url(r'^press/$', Press_View.as_view(), name='press'),
    url(r'^contact/$', Contact_View.as_view(), name='contact'),

    # main
    url(r'^rss_data.log/$', login_required(RSS_View), name='data_log'),
    url(r'^', login_required(CourseSelector_View.as_view()), name='none'),
)

