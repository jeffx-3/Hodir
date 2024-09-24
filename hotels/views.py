from django.shortcuts import render
from .models import Restaurant
# Create your views here.
def home(request):
    return render(request, 'hotels/templates/home.html')

##search view
def search_restaurants(request):
    query = request.GET.get('q', '')  # Get the search term from the query parameters
    if query:
        results = Restaurant.objects.filter(name__icontains=query)
    else:
        results = Restaurant.objects.none()  # No search results if no query
    
    context = {
        'results': results,
        'query': query,
    }
    
    return render(request, 'search_results.html', context)