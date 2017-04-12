from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from frontend import views


urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    # url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),

    # url(r'^$', views.index, name='index'),
    url(r'^$', views.index, name='index'),

    url(r'^', include('frontend.urls')),
    url(r'^', include('users.urls')),
    url(r'^', include('travel_plans.urls')),


    # url(r'^openid/(.*)', SessionConsumer()),
)
