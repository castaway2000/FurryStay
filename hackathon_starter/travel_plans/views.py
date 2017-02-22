from django.shortcuts import render, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from .models import LocationVisit
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
            kwargs["location__name"] = data.get("location")

        if data.get("date_start"):
            kwargs["date_start__gte"]=datetime.datetime.strptime(data.get("date_start"), "%d-%b-%Y").date()
        # else:
        #     kwargs["date_start__gte"] = datetime.datetime.today().date()

        if data.get("date_end"):
            kwargs["date_end__lte"]=datetime.datetime.strptime(data.get("date_end"), "%d-%b-%Y").date()


        location_visits = LocationVisit.objects.filter(**kwargs)\
            .values("location__name", "date_start", "date_end", "user__username", "user__email")

        print (kwargs)
        print (location_visits)

        context = {
            'location_visits' : location_visits,
        }
        return render(request, 'travel_plans/search.html', context)
    else:
        return HttpResponseRedirect(reverse('index'))