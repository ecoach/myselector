from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, render
from django.views.generic import TemplateView
from mynav.nav import main_nav
#from myselector.nav_info import NavInfo
#from myselector.models import RSSLog, ELog

def test1(request, **kwargs):
    return HttpResponse("You're looking at the selector test page")

def course_select_view(request, **kwargs):
    
    return render(request, 'myselector/mycourse.html', {
        "main_nav": main_nav(request.user, 'coaches')
    })

def mylogout(request):
    return HttpResponseRedirect("https://weblogin.umich.edu/cgi-bin/logout")

def mylogin(request, **kwargs):
    return render_to_response('django.contrib.auth.views.login')


