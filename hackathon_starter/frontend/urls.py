from django.conf.urls import patterns, url, include
from rest_framework.routers import DefaultRouter
import views


urlpatterns = patterns(

    url(r'^index/$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^coc/$', views.code_of_conduct, name='code_of_conduct'),
    url(r'^contact/$', views.contact_us, name='contact'),
    url(r'^promise/$', views.travelers_promise, name='travelers_promise'),
    url(r'^privacy/$', views.privacy_policy, name='privacy'),
    url(r'^terms/$', views.terms_of_service, name='tos'),
    url(r'^api/$', views.api_examples, name='api'),

)
