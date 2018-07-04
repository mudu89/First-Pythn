from django.urls import path
from django.conf.urls import url, include
from django.views.generic import TemplateView
from django.contrib.auth.views import login, logout
from django.contrib import admin


urlpatterns =[
        url(r'$', login,{'template_name':'index.html'},name="home"),

        ]