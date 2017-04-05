# Django
from django.shortcuts import render
from django.contrib.auth import logout
from django.template import RequestContext, loader
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

# Django REST Framework
from rest_framework import viewsets, mixins

# Scripts
from scripts.twitter import TwitterOauthClient
from scripts.facebook import *
from scripts.googlePlus import *


# Python
# from requests_oauth2 import OAuth2 as oauth
import oauth2 as oauth
import simplejson as json
import requests


# Models
from models import *
from serializers import SnippetSerializer
from forms import UserForm

profile_track = None
# getTwitter = TwitterOauthClient(settings.TWITTER_CONSUMER_KEY, settings.TWITTER_CONSUMER_SECRET, settings.TWITTER_ACCESS_TOKEN, settings.TWITTER_ACCESS_TOKEN_SECRET)
# getFacebook = FacebookOauthClient(settings.FACEBOOK_APP_ID, settings.FACEBOOK_APP_SECRET)
# getGoogle = GooglePlus(settings.GOOGLE_PLUS_APP_ID, settings.GOOGLE_PLUS_APP_SECRET)


##################
#   userpage     #
##################

def userpage(request, username=None):
    user = request.user

    print username

    if username:
        try:
            user = User.objects.get(username=username)
        except:
            return render(request, 'users/userpage.html')

    #if no username is specified in url, it is possible to display info just for current user
    elif not user.is_anonymous():
        user = request.user
    else:
        return render(request, 'users/userpage.html')

    username = user.username

    location = "new york city"
    interests = 'sports, mountain climbing, bleh, foobar, coding'
    accomodation = ['house', 'double bed', 'futon']
    # for pictures: http://ashleydw.github.io/lightbox/
    
    YELP_CONSUMER_KEY = '9PLzBaT21UbHC7MCS5eYkQ'
    YELP_CONSUMER_SECRET = 'I9NC-0JB2Mc7H6kHD_Y-D0Lqfuk'
    YELP_ACCESS_KEY = 'go7gUc6VZnAinnMRg9BB9TQ2NcUEtAEE'
    YELP_ACCESS_SECRET = 'yMzMcMAiMOQyHQTWKfrqJpdQEBs'
    consumer_key = YELP_CONSUMER_KEY
    consumer_secret = YELP_CONSUMER_SECRET
    access_key = YELP_ACCESS_KEY
    access_secret = YELP_ACCESS_SECRET
    
    
    site = 'https://api.yelp.com/v2/search'
    consumer = oauth.Consumer(consumer_key, consumer_secret)
    access_token = oauth.Token(access_key, access_secret)
    client = oauth.Client(consumer, access_token)
    endpoint = 'https://api.yelp.com/v2/search/'
    search_terms = '?term=tourist attractions&location='+ location + \
                   '&limit=10&radius_filter=10000'
    responce, data = client.request(endpoint+search_terms)
    attractions = json.loads(data)['businesses']

    listofattractions = list()
    for n in xrange(0, len(attractions)):
        listofattractions.append(attractions[n]['name'])

    context = {'username': username,
               'location': location,
               'yelp': listofattractions,
               'interests': interests,
               'accomodation': accomodation
               }
    return render(request, 'users/userpage.html', context)


##################
#  edit userpage #
##################

def edit_userpage(request, username=None):
    user = request.user
    if username:
        try:
            user = User.objects.get(username=username)
        except:
            return render(request, 'users/edit_userpage.html')
    # if no username is specified in url, it is possible to display info just for current user
    elif not user.is_anonymous():
        user = request.user
    else:
        return render(request, 'users/edit_userpage.html')
    username = user.username
    interests = 'sports, mountain climbing, bleh, foobar, coding'
    accomodation = "house, wifi, etc..."
    about = 'About me...'
    # for pictures: http://ashleydw.github.io/lightbox/
    context = {'username': username,
               'interests': interests,
               'accomodation': accomodation,
               'about': about
               }
    return render(request, 'users/edit_userpage.html', context)

##################
#   dashboard   #
##################

def user_dashboard(request, username=None):
    user = request.user
    if username:
        try:
            user = User.objects.get(username=username)
        except:
            return render(request, 'users/dashboard.html')
    # if no username is specified in url, it is possible to display info just for current user
    elif not user.is_anonymous():
        user = request.user
    else:
        return render(request, 'users/dashboard.html')
    username = user.username
    schedule = "here be dragons between january and december"
    messages = "To from and inbetween"

    # for pictures: http://ashleydw.github.io/lightbox/
    context = {'username': username,
               'schedule': schedule,
               'messages': messages,
               }
    return render(request, 'users/dashboard.html', context)


#########################
# Snippet RESTful Model #
#########################

class CRUDBaseView(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  viewsets.GenericViewSet):
    pass

class SnippetView(CRUDBaseView):
    serializer_class = SnippetSerializer
    queryset = Snippet.objects.all()


######################
# Registration Views #
######################

def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
            return HttpResponseRedirect('/login/')
        else:
            print user_form.errors
    else:
        user_form = UserForm()

    return render(request,
                  'users/register.html',
                  {'user_form': user_form, 'registered': registered})



# HOST
def host_register(request):
    gRegister = False
    user = request.user
    if user.is_authenticated == True:
        if request.method == 'POST':
            print "Current user", u
            host_form = UserForm(data=request.POST, instance=user)
            if host_form.is_valid():
                hostf = host_form.save()
                hostf.set_password(hostf.password)
                hostf.save()
                gRegister = True
                return HttpResponseRedirect('/login/')
            else:
                print host_form.errors
                
        guide_form = UserForm()
        context = {'guide_form': guide_form, 'registered': gRegister}
        return render(request, 'users/host.html', context)

        
    else:
        if request.method == 'POST':
            host_form = UserForm(data=request.POST)
            if host_form.is_valid():
                hostf = host_form.save()
                hostf.set_password(hostf.password)
                hostf.save()
                gRegister = True
                return HttpResponseRedirect('/login/')
            else:
                print host_form.errors
                
        guide_form = UserForm()
        context = {'guide_form': guide_form, 'registered': gRegister}
        return render(request, 'users/host.html', context)


######################
#       Login        #
######################
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                return HttpResponse("Your Django Hackathon account is disabled.")
        else:
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'users/login.html', {})

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')
