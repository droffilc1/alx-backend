#!/usr/bin/env python3
""" 2-lifo_cache
Implements LIFO caching.
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """A class LIFOCache that inherits from BaseCaching
    and is a caching system.
    """

    def __init__(self):
        """Initialize"""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """Add item in the cache."""
        if key is not None and item is not None:
            # Remove the old key to update its position in the order list
            if key in self.cache_data:
                self.order.remove(key)
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Remove last item from the cache
                last_key = self.order.pop()
                del self.cache_data[last_key]
                print(f"DISCARD: {last_key}")
        # Add new item in the cache and order list
        self.cache_data[key] = item
        self.order.append(key)

    def get(self, key):
        """Get an item by key."""
        return self.cache_data.get(key, None)
