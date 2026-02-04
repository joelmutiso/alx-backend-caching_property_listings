import logging
from django_redis import get_redis_connection

# Set up logging to track metrics in your console
logger = logging.getLogger(__name__)

def get_redis_cache_metrics():
    """
    Connects to Redis, retrieves keyspace hit/miss metrics,
    calculates the hit ratio, and returns the stats.
    """
    try:
        # 1. Connect to the raw Redis client via django_redis
        redis_conn = get_redis_connection("default")
        
        # 2. Get the INFO dictionary from Redis
        info = redis_conn.info()
        
        # 3. Extract keyspace_hits and keyspace_misses
        hits = info.get('keyspace_hits', 0)
        misses = info.get('keyspace_misses', 0)
        
        # 4. Calculate Hit Ratio (Avoid division by zero)
        total_requests = hits + misses
        hit_ratio = (hits / total_requests) if total_requests > 0 else 0.0
        
        metrics = {
            "keyspace_hits": hits,
            "keyspace_misses": misses,
            "hit_ratio": hit_ratio
        }
        
        # 5. Log metrics for observability
        logger.info(f"Cache Metrics: Hits={hits}, Misses={misses}, Ratio={hit_ratio:.2f}")
        
        return metrics

    except Exception as e:
        logger.error(f"Failed to retrieve Redis metrics: {e}")
        return {"error": "Could not connect to Redis"}