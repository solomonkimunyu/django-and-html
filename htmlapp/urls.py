from django.urls import path
from .views import HomeView, AboutView, LearnHtmlView, TutorialView

urlpatterns = [
    path('', HomeView.as_view(), name = 'home'),
    path('about/', AboutView.as_view(), name = 'about'),
    path('learn/', LearnHtmlView.as_view(), name = 'learn'), 
    path('tutorial/', TutorialView.as_view(), name = 'tutorial')
]