from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.views.generic import TemplateView
#from myselector.nav_info import NavInfo
#from myselector.models import RSSLog, ELog
#from django.contrib.auth.models import User

def test1(request, **kwargs):
    return HttpResponse("You're looking at the selector test page")

class CourseSelector_View(TemplateView):
    template_name = "myselector/mycourse.html"

    def dispatch(self, request, *args, **kwargs):
        # psudo constructor
        #Log_Request(request)
        #self.m_nav = NavInfo(request.path)
        return super(CourseSelector_View, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(CourseSelector_View, self).get_context_data(**kwargs)
        #context["nav"] = self.m_nav       
        return context

def mylogout(request):
    return HttpResponseRedirect("https://weblogin.umich.edu/cgi-bin/logout")

def mylogin(request, **kwargs):
    return render_to_response('django.contrib.auth.views.login')


