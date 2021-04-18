from django.shortcuts import render
from django.http import HttpResponse

from listings.models import Listing

from realtors.models import Realtor

from listings.choices import bedroom_choices,price_choices,state_choices

def index(request):
    # get the latest Listings
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]

    # pass it to the context 
    context = {
        
        'listings':listings,
        'bedroom_choices':bedroom_choices,
        'price_choices' : price_choices,
        'state_choices' : state_choices
    }

    # pass the contect to teh render 
    return render(request,'pages/index.html' , context)
   

def about(request):
    # get the realtor for the database
    realtors = Realtor.objects.order_by('-hire_date')[:3]

    # get the seller of the month
    mvp_realtors = Realtor.objects.filter(is_mvp=True)

    # pass them to the context
    context = {
        'realtors': realtors,
        'mvp_realtors' : mvp_realtors
    }
    #  reder static html 
    return render(request, 'pages/about.html' , context)
