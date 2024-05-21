#!/usr/bin/env python3
"""1-fifo_cache
Implements FIFO caching.
"""

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """A class FIFOCache that inherits from BaseCaching and is
      a caching system.
    """

    def __init__(self):
        """Initialize."""
        super().__init__()

    def put(self, key, item):
        """Add an item in the cache."""
        if key or item is None:
            pass
        self.cache_data[key] = item
        if len(self.cache_data.items()) > BaseCaching.MAX_ITEMS:
            # discards the first item put in cache(FIFO algorithm)
            first_item = next(iter(self.cache_data))
            del self.cache_data[first_item]
            print(f"DISCARD: {first_item}")

    def get(self, key):
        """Get an item by key."""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
