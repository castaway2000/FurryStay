from django.conf.urls import patterns, url, include
from rest_framework.routers import DefaultRouter

import views

router = DefaultRouter()
router.register(r'snippets', views.SnippetView)

urlpatterns = patterns('',
    url(r'^', include(router.urls)),

    url(r'^search_results/$', views.search_results, name='search_results'),

    url(r'^index/$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^coc/$', views.code_of_conduct, name='code_of_conduct'),
    url(r'^contact/$', views.contact_us, name='contact'),
    url(r'^promise/$', views.travelers_promise, name='travelers_promise'),
    url(r'^privacy/$', views.privacy_policy, name='privacy'),
    url(r'^terms/$', views.terms_of_service, name='tos'),
    url(r'^host/$', views.host_register, name='host'),
    url(r'^userpage/$', views.userpage, name='userpage'),
    url(r'^search/$', views.searchEngine, name='search'),
    url(r'^api/$', views.api_examples, name='api'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^twitter/$', views.twitter, name='twitter'),
    url(r'^twitterTweets/$', views.twitterTweets, name='twitterTweets'),
    url(r'^twitter_login/$', views.twitter_login, name='twitter_login'),
    url(r'^facebook_login/$', views.facebook_login, name='facebook_login'),
    url(r'^facebook/$', views.facebook, name='facebook'),
    url(r'^google_login/$', views.google_login, name='google_login'),
    url(r'^google/$', views.googlePlus, name='googlePlus')
)
