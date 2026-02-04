from django.core.cache import cache
from .models import Property

def get_all_properties():
    """
    Fetches all properties using low-level caching.
    Checks Redis for 'all_properties' key first.
    If not found, fetches from DB and caches it for 1 hour (3600 seconds).
    """
    # 1. Check Redis for the key 'all_properties'
    queryset = cache.get('all_properties')
    
    # 2. If not found in cache, fetch from Database
    if queryset is None:
        queryset = Property.objects.all()
        # 3. Store the queryset in Redis for 3600 seconds (1 hour)
        cache.set('all_properties', queryset, 3600)
    
    return queryset