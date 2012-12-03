from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.views.generic import TemplateView
from myselector.nav_info import NavInfo
from myselector.models import RSSLog, ELog
#from django.contrib.auth.models import User

def test1(request, **kwargs):
    return HttpResponse("You're looking at the selector test page")

class CourseSelector_View(TemplateView):
    template_name = "myselector/mycourse.html"

    def dispatch(self, request, *args, **kwargs):
        # psudo constructor
        Log_Request(request)
        self.m_nav = NavInfo(request.path)
        return super(CourseSelector_View, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(CourseSelector_View, self).get_context_data(**kwargs)
        context["nav"] = self.m_nav       
        return context

class About_View(TemplateView):
    template_name = "myselector/about.html"

    def dispatch(self, request, *args, **kwargs):
        # psudo constructor
        Log_Request(request)
        self.m_nav = NavInfo(request.path)
        return super(About_View, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(About_View, self).get_context_data(**kwargs)
        context["nav"] = self.m_nav       
        return context

class Tailoring_View(TemplateView):
    template_name = "myselector/tailoring.html"

    def dispatch(self, request, *args, **kwargs):
        # psudo constructor
        Log_Request(request)
        self.m_nav = NavInfo(request.path)
        return super(Tailoring_View, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(Tailoring_View, self).get_context_data(**kwargs)
        context["nav"] = self.m_nav       
        return context

class Team_View(TemplateView):
    template_name = "myselector/team.html"

    def dispatch(self, request, *args, **kwargs):
        # psudo constructor
        Log_Request(request)
        self.m_nav = NavInfo(request.path)
        return super(Team_View, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(Team_View, self).get_context_data(**kwargs)
        context["nav"] = self.m_nav       
        return context

class Press_View(TemplateView):
    template_name = "myselector/press.html"

    def dispatch(self, request, *args, **kwargs):
        # psudo constructor
        Log_Request(request)
        self.m_nav = NavInfo(request.path)
        return super(Press_View, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(Press_View, self).get_context_data(**kwargs)
        context["nav"] = self.m_nav       
        return context

class Contact_View(TemplateView):
    template_name = "myselector/contact.html"

    def dispatch(self, request, *args, **kwargs):
        # psudo constructor
        Log_Request(request)
        self.m_nav = NavInfo(request.path)
        return super(Contact_View, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(Contact_View, self).get_context_data(**kwargs)
        context["nav"] = self.m_nav       
        return context

def mylogout(request):
    return HttpResponseRedirect("https://weblogin.umich.edu/cgi-bin/logout")

def mylogin(request, **kwargs):
    return render_to_response('django.contrib.auth.views.login')

def RSS_View(request):
    import datetime
    # do a little logging...
    rlink = request.GET['link'] 
    rarticle = request.GET['article'] 
    rwho = request.user.username
    rwhen = datetime.datetime.now()

    log = RSSLog(who=request.user, mwhen=rwhen, link=rlink, article=rarticle)
    log.save()

    return HttpResponse("We want to record which articles are of interest")
 
def Log_Request(request):
    import datetime
    # do a little logging...
    rwhat = request.path
    rwho = request.user.username
    rwhen = datetime.datetime.now()

    log = ELog(who=request.user, mwhen=rwhen, what=rwhat)
    log.save()       


