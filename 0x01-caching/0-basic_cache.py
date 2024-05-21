#!/usr/bin/env python3
"""0-basic_cache.
Implements a basic cache.
"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """A class BasicCache that inherits from BaseCaching."""

    def put(self, key, item):
        """Add an item to the cache."""
        if key or item is None:
            pass
        self.cache_data[key] = item

    def get(self, key):
        """Get an item by key."""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
