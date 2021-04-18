from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Listing

def index(req):
   listings = Listing.objects.all()
   paginator = Paginator(listings , 2)
   page = req.Get.get('page')
   paged_listings = paginator.get_page(page)
   context = {
       'listings' : paged_listings
   }
   return render(req, 'listings/listings.html' , context)

def listing(req ,listing_id):
    return render(req, 'listings/listing.html')

def search(req):
    return render(req, 'listings/search.html')