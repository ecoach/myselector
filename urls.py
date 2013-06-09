from django.conf.urls.defaults import patterns, include, url
from .views import *
from django.contrib.auth.decorators import login_required

#from mydata4 import urls

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # admin
    url(r'^admin/', include(admin.site.urls)),

    # login / logout
    #url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout', 'mylogout'),

    # coaches
    #url(r'^mts0/$', login_required(mydata0.urls)),
    #url(r'^mts1/$', login_required(mydata1.urls)),
    #url(r'^mts2/$', login_required(mydata2.urls)),
    #url(r'^mts3/$', login_required(mydata3.urls)),
    #url(r'^mts4/$', login_required(mydata4.urls)),
    #url(r'^mts5/$', login_required(mydata5.urls)),

    # main
    url(r'^', login_required(CourseSelector_View.as_view()), name='none'),
)

