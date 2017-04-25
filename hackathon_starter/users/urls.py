from django.conf.urls import patterns, url, include
from rest_framework.routers import DefaultRouter

import views

router = DefaultRouter()
router.register(r'snippets', views.SnippetView)

urlpatterns = patterns('',
    url(r'^', include(router.urls)),

    url(r'^host/$', views.host_register, name='host'),
    url(r'^chooser$', views.chooser, name='chooser'),
    url(r'^userpage/$', views.userpage, name='my_userpage'),
    url(r'^edit_userpage/$', views.edit_userpage, name='edit_userpage'),
    url(r'^user_settings/$', views.user_settings, name='user_settings'),
    url(r'^dashboard/$', views.user_dashboard, name='dashboard'),
    url(r'^userpage/(?P<username>\w+)/$', views.userpage, name='userpage'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    # url(r'^twitter/$', views.twitter, name='twitter'),
    # url(r'^twitterTweets/$', views.twitterTweets, name='twitterTweets'),
    # url(r'^twitter_login/$', views.twitter_login, name='twitter_login'),
    # url(r'^facebook_login/$', views.facebook_login, name='facebook_login'),
    # url(r'^facebook/$', views.facebook, name='facebook'),
    # url(r'^google_login/$', views.google_login, name='google_login'),
    # url(r'^google/$', views.googlePlus, name='googlePlus')
)
