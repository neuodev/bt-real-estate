from django.shortcuts import render
from django.http import HttpResponse

from listings.models import Listing

def index(request):
    # get the latest Listings
    listings = Listing.objects.order_by('-list_date')[:3]
    # pass it to the context 
    context = {'listings':listings}
    # pass the contect to teh render 
    return render(request,'pages/index.html' , context)
   

def about(request):
    return render(request, 'pages/about.html')
