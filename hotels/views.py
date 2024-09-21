from django.shortcuts import render
from .models import restaurant
# Create your views here.
def home(request):
    return render(request, 'hotels/templates/home.html')

##search view
def search_restaurants(request):
    query = request.GET.get('q')  # Get the search term from the query parameters
    if query:
        results = restaurant.objects.filter(name__icontains=query) | restaurant.objects.filter(id__icontains=query)
        ##print("Found {results.count()} results")
    else:
        results = restaurant.objects.none()  # No search results if no query
    
    context = {
        'results': results,
        'query': query,
    }
    return render(request, 'search_results.html', context)