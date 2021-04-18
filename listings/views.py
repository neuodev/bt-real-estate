from django.shortcuts import render , get_object_or_404
from django.core.paginator import Paginator , EmptyPage, PageNotAnInteger
from .models import Listing

def index(req):
    # get the listing from the database 
   listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    #    add pagination 
   paginator = Paginator(listings , 3)
   page = req.GET.get('page')
   paged_listings = paginator.get_page(page)
    #    pass the pagination for the listing
   context = {
       'listings' : paged_listings
   }
   return render(req, 'listings/listings.html' , context)

def listing(req ,listing_id):
    # get listing by id 
    single_listing = get_object_or_404(Listing,pk=listing_id)
    # pass it to the context 
    context = {
        'listing': single_listing
    }
    # render the page 
    return render(req, 'listings/listing.html' , context)

def search(req):
    return render(req, 'listings/search.html')