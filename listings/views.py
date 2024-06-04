from django.shortcuts import render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from .models import Listing

# Create your views here.
def index(request):
    listings = Listing \
        .objects \
        .order_by('-list_date') \
        .filter(is_published=True)
    
    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    return render(request, 'listings/listings.html', context={'listings': paged_listings})

def listing(request, listing_id):
    return render(request, 'listings/listing.html')

def search(request):
    return render(request, 'listings/search.html')
