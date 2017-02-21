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
from forms import UserForm, HostForm

profile_track = None
getTwitter = TwitterOauthClient(settings.TWITTER_CONSUMER_KEY, settings.TWITTER_CONSUMER_SECRET, settings.TWITTER_ACCESS_TOKEN, settings.TWITTER_ACCESS_TOKEN_SECRET)
getFacebook = FacebookOauthClient(settings.FACEBOOK_APP_ID, settings.FACEBOOK_APP_SECRET)
getGoogle = GooglePlus(settings.GOOGLE_PLUS_APP_ID, settings.GOOGLE_PLUS_APP_SECRET)



def search_results(request):
    return render(request, 'search_results.html', locals())


##################
#   Index Page   #
##################
def index(request):
    print "index: " + str(request.user)
    if not request.user.is_active:
        if request.GET.items():
            if profile_track == 'twitter':
                oauth_verifier = request.GET['oauth_verifier']
                getTwitter.get_access_token_url(oauth_verifier)
                try:
                    user = User.objects.get(username = getTwitter.username + '_twitter')#(username=getTwitter.username)
                except User.DoesNotExist:
                    username = getTwitter.username + '_twitter'
                    new_user = User.objects.create_user(username, username+'@madewithtwitter.com', 'password')
                    new_user.save()
                    profile = TwitterProfile(user = new_user,oauth_token = getTwitter.oauth_token, oauth_token_secret= getTwitter.oauth_token_secret, twitter_user=getTwitter.username)
                    profile.save()
                user = authenticate(username=getTwitter.username+'_twitter', password='password')
                login(request, user)

            elif profile_track == 'facebook':
                code = request.GET['code']
                getFacebook.get_access_token(code)
                userInfo = getFacebook.get_user_info()
                username = userInfo['first_name'] + userInfo['last_name']

                try:
                    user = User.objects.get(username=username+'_facebook')
                except User.DoesNotExist:
                    new_user = User.objects.create_user(username+'_facebook', username+'@madewithfacbook', 'password')
                    new_user.save()

                    try:
                        profile = FacebookProfile.objects.get(user=new_user.id)
                        profile.access_token = getFacebook.access_token
                    except:
                        profile = FacebookProfile()
                        profile.user = new_user
                        profile.fb_user_id = userInfo['id']
                        profile.profile_url = userInfo['link']
                        profile.access_token = getFacebook.access_token
                    profile.save()
                user = authenticate(username=username+'_facebook', password='password')
                login(request, user)

            elif profile_track == 'google':
                code = request.GET['code']
                state = request.GET['state']
                getGoogle.get_access_token(code, state)
                userInfo = getGoogle.get_user_info()
                username = userInfo['given_name'] + userInfo['family_name']

                try:
                    user = User.objects.get(username=username+'_google')
                except User.DoesNotExist:
                    new_user = User.objects.create_user(username+'_google', username+'@madewithgoogleplus', 'password')
                    new_user.save()

                    try:
                        profle = GoogleProfile.objects.get(user = new_user.id)
                        profile.access_token = getGoogle.access_token
                    except:
                        profile = GoogleProfile()
                        profile.user = new_user
                        profile.google_user_id = userInfo['id']
                        profile.access_token = getGoogle.access_token
                        profile.profile_url = userInfo['link']
                    profile.save()
                user = authenticate(username=username+'_google', password='password')
                login(request, user)
    else:
        if request.GET.items():
            user = User.objects.get(username = request.user.username)
            if profile_track == 'twitter':
                oauth_verifier = request.GET['oauth_verifier']
                getTwitter.get_access_token_url(oauth_verifier)
                try:
                    twitterUser = TwitterProfile.objects.get(user = user.id)
                except TwitterProfile.DoesNotExist:
                    profile = TwitterProfile(user = user, oauth_token = getTwitter.oauth_token, oauth_token_secret= getTwitter.oauth_token_secret, twitter_user=getTwitter.username)
                    profile.save()
    context = {'hello': 'world'}
    return render(request, 'index.html', context)


##################
#   About Page   #
##################

def about(request):
    context = {'title': 'About OpenStay'}
    return render(request, 'about.html', context)

##################
#  API Examples  #
##################

def api_examples(request):
    context = {'title': 'API Examples Page'}
    return render(request, 'api_examples.html', context)


########################
#   become host Page   #
########################

def host(request):
    context = {'title': 'host with OpenStay'}
    return render(request, 'host.html', context)
    
########################
#   code of conduct    #
########################

def code_of_conduct(request):
    context = {'title': 'OpenStay Code Of Conduct'}
    return render(request, 'CodeOfConduct.html', context)

########################
#     Contact info     #
########################

def contact_us(request):
    context = {'title': 'Contact Openstay'}
    return render(request, 'contact.html', context)

########################
#     pivacy policy    #
########################

def privacy_policy(request):
    context = {'title': 'OpenStay Privacy policy'}
    return render(request, 'privacy.html', context)

########################
#    Terms of service  #
########################

def terms_of_service(request):
    context = {'title': 'OpenStay ToS'}
    return render(request, 'terms.html', context)


#########################
# The Travelers Promise #
#########################

def travelers_promise(request):
    context = {'title': 'The Travelers Promise'}
    return render(request, 'travelerspromise.html', context)

##################
#   userpage     #
##################

def userpage(request):
    user = User.objects.all()
    listofattractions = []
    for u in user:
        name = u.username
        

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
    for n in xrange(0, len(attractions)):
        listofattractions.append(attractions[n]['name'])
    context = {'username': name, 'location': location, 'yelp': listofattractions,
               'interests': interests, 'accomodation': accomodation}
    return render(request, 'userpage.html', context)


#################
# search engine #
#################

def searchEngine(request):
    '''
    This is an example of getting basic user info and display it
    '''
    user = User.objects.all()
    listofusers = []
    for u in user:
        listofusers.append(u)
    return render(request, 'search.html', {'results' : listofusers})

#################
#  FACEBOOK API #
#################

def facebook(request):
    '''
    This is an example of getting basic user info and display it
    '''
    userInfo = getFacebook.get_user_info()
    return render(request, 'facebookAPIExample.html', {'userInfo' : userInfo})

#################
#  GOOGLE API   #
#################
def googlePlus(request):

    userInfo = getGoogle.get_user_info()
    return render(request, 'googlePlus.html', {'userInfo' : userInfo})

####################
#   TWITTER API    #
####################

def twitter(request):
    if getTwitter.is_authorized:
        value = getTwitter.get_trends_available(settings.YAHOO_CONSUMER_KEY)
    else:
        global profile_track
        profile_track = 'twitter'
        twitter_url = getTwitter.get_authorize_url()
        return HttpResponseRedirect(twitter_url)

    context ={'title': 'twitter', 'value': value}
    return render(request, 'twitter.html', context)

def twitterTweets(request):
    print getTwitter.is_authorized
    if getTwitter.is_authorized:
        if request.method == 'GET':
            if request.GET.items():
                tweets = request.GET.get('tweets')
                content, jsonlist = getTwitter.get_tweets(tweets)
            else:
                content, jsonlist = '', ''
    else:
        global profile_track
        profile_track = 'twitter'
        twitter_url = getTwitter.get_authorize_url()
        return HttpResponseRedirect(twitter_url)

    context ={'title': 'twitter tweet', 'content': content, 'data': jsonlist}
    return render(request, 'twitter_tweet.html', context)


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
                  'register.html',
                  {'user_form': user_form, 'registered': registered})



# HOST
def host_register(request):
    gRegister = False
    if request.method == 'POST':
        host_form = HostForm(data=request.POST)
        if host_form.is_valid():
            user = host_form.save()
            user.set_password(user.password)
            user.save()
            gRegister = True
            return HttpResponseRedirect('/api/')
        else:
            print host_form.errors
    else:
        guide_form = HostForm()
    context = {'guide_form': guide_form, 'registered': gRegister}
    return render(request, 'host.html', context)


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
        return render(request, 'login.html', {})

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')


def twitter_login(request):
    global profile_track
    profile_track = 'twitter'
    twitter_url = getTwitter.get_authorize_url()
    return HttpResponseRedirect(twitter_url)


def facebook_login(request):
    global profile_track
    profile_track = 'facebook'
    facebook_url = getFacebook.get_authorize_url()
    return HttpResponseRedirect(facebook_url)


def google_login(request):
    global profile_track
    profile_track = 'google'
    google_url = getGoogle.get_authorize_url()
    return HttpResponseRedirect(google_url)
