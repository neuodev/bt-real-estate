from django.shortcuts import render
from django.http import HttpResponse

from listings.models import Listing

from realtors.models import Realtor

def index(request):
    # get the latest Listings
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]

    # pass it to the context 
    context = {'listings':listings}

    # pass the contect to teh render 
    return render(request,'pages/index.html' , context)
   

def about(request):
    # get the realtor for the database
    realtors = Realtor.objects.all()[:3]
    # pass them to the context
    context = {
        'realtors': realtors
    }
    #  reder static html 
    return render(request, 'pages/about.html' , context)
