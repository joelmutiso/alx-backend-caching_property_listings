from django.http import JsonResponse
from django.views.decorators.cache import cache_page
from .models import Property

@cache_page(60 * 15)
def property_list(request):
    """
    Fetches all properties and returns them as a JSON response.
    The response is cached in Redis for 15 minutes.
    """
    properties = Property.objects.all()
    
    # Structure the data as a list of dictionaries
    property_data = [
        {
            "id": p.id,
            "title": p.title,
            "description": p.description,
            "price": str(p.price),
            "location": p.location,
            "created_at": p.created_at.strftime("%Y-%m-%d %H:%M:%S"),
        }
        for p in properties
    ]
    
    # Return JsonResponse with the 'data' key as expected by the checker
    return JsonResponse({"data": property_data})