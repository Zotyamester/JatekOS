from django.urls import path
from django.views.generic.base import TemplateView

from . import views

app_name = 'main'
urlpatterns = [
    path('', views.home, name='home'),
    path('faq/', TemplateView.as_view(template_name='main/faq.html'), name='faq'),
    path('about', TemplateView.as_view(
        template_name='main/about.html'), name='about'),
    path('privacy/', TemplateView.as_view(template_name='main/privacy.html'), name='privacy'),
]
