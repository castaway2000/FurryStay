from django.shortcuts import render, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from .models import LocationVisit
from users.models import HostRegistration, UserProfile
import datetime


#################
# search engine #
#################
def search(request):
    '''
    This is an example of getting basic user info and display it
    '''
    if request.POST:
        data = request.POST
        print data
        kwargs = dict()
        if data.get("location"):
            print True
            kwargs["city"] = data.get("location")
            
        # if data.get("date_start"):
        #     print True
        #     kwargs["date_start__gte"]=datetime.datetime.strptime(data.get("date_start"), "%d-%b-%Y").date()
        # # else:
        # #     kwargs["date_start__gte"] = datetime.datetime.today().date()

        # if data.get("date_end"):
        #     print True
        #     kwargs["date_end__lte"]=datetime.datetime.strptime(data.get("date_end"), "%d-%b-%Y").date()
        location_visits = HostRegistration.objects.filter(**kwargs)\
            .values("city", "user__username", "user__id")#, "user__username", "user__email")
        profiles = []
        profile_info = {'username': None, 'city': None, 'image': None, "interests": None}
        for u in location_visits:
            print u['user__id']
            profile =  UserProfile.objects.get(user_id=u['user__id'])
            print profile.profile_image
            profile_info['username'] = (u['user__username'])
            profile_info['city'] = (u['city'])
            profile_info['image'] = (profile.profile_image.url)
            profile_info['interests'] = (profile.interests)
            profiles.append(profile_info)
            profile_info = {'username': None, 'city': None, 'image': None, "interests": None}
        print (kwargs)
        print ('loc ', profiles)

        context = {
            'location_visits': location_visits,
            'profiles': profiles
        }
        return render(request, 'travel_plans/search.html', context)
    else:
        return HttpResponseRedirect(reverse('index'))