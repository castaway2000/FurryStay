from django.conf.urls import patterns, url, include
from rest_framework.routers import DefaultRouter

import views

urlpatterns = patterns('',
    url(r'^search/$', views.search, name='search'),
)
