#!/usr/bin/env python3
"""1-fifo_cache
Implements FIFO caching.
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """A class FIFOCache that inherits from BaseCaching and is
      a caching system.
    """

    def __init__(self):
        """Initialize."""
        super().__init__()

    def put(self, key, item):
        """Add an item in the cache."""
        if key is not None or item is not None:
            if len(self.cache_data.items()) > BaseCaching.MAX_ITEMS:
                # discards the first item put in cache(FIFO algorithm)
                first_key = next(iter(self.cache_data))
                print(f"DISCARD: {first_key}")
                self.cache_data.pop(first_key)
            self.cache_data[key] = item

    def get(self, key):
        """Get an item by key."""
        return self.cache_data.get(key, None)
