from django.shortcuts import render , get_object_or_404
from django.core.paginator import Paginator , EmptyPage, PageNotAnInteger
from .models import Listing

from .choices import bedroom_choices,price_choices,state_choices

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
    # get all listings
    query_listings = Listing.objects.order_by('-list_date')
    # keywords
    if 'keywords' in req.GET:
        keywords = req.GET['keywords']
        if keywords:
           query_listings= query_listings.filter(description__icontains=keywords)
    # city 
    if 'city' in req.GET:
        city = req.GET['city']
        if city: 
            query_listings = query_listings.filter(city__iexact=city)
    # price 
    if 'price' in req.GET:
        price = req.GET['price']
        if price: 
            query_listings = query_listings.filter(price__lte=int(price))
    # bedrooms 
    if 'bedrooms' in req.GET:
        bedrooms = req.GET['bedrooms']
        if bedrooms: 
            query_listings = query_listings.filter(bedrooms__lte=int(bedrooms))
    # state 
    if 'state' in req.GET:
        state = req.GET['state']
        if state: 
            query_listings = query_listings.filter(state__iexact=state)
    context = {
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'state_choices' : state_choices,
        'listings': query_listings ,
        'values': req.GET
    }
    return render(req, 'listings/search.html' , context)