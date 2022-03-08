from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class HomeView(TemplateView):
    template_name = 'home.html'
    
class AboutView(TemplateView):
    template_name = 'about.html'
    
class LearnHtmlView(TemplateView):
    template_name = 'learn.html'

class TutorialView(TemplateView):
    template_name = 'tutorial.html'
