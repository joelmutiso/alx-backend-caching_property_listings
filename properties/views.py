from django.http import JsonResponse
from .utils import get_all_properties

def property_list(request):
    """
    Returns property list using the low-level cache utility.
    """
    # Use the utility instead of Property.objects.all()
    properties = get_all_properties()
    
    property_data = [
        {
            "id": p.id,
            "title": p.title,
            "description": p.description,
            "price": str(p.price),
            "location": p.location,
        }
        for p in properties
    ]
    
    return JsonResponse({"data": property_data})