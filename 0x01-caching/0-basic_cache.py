#!/usr/bin/env python3
"""0-basic_cache.
Implements a basic cache.
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """BasicCache is a caching system that inherits from BaseCaching.
    This caching system doesn't have a limit on the number of items stored.
    """

    def put(self, key, item):
        """Add an item to the cache.

        If key or item is None, this method does nothing.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Get an item by key.

        If key is None or if the key doesn't exist in self.cache_data,
        return None.
        """
        return self.cache_data.get(key, None)
