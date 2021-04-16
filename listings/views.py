from django.shortcuts import render

def index(req):
    render(req, 'listings/listings.html')

def listing(req):
    render(req, 'listings/listing.html')

def search(req):
    render(req, 'listings/search.html')