#!/usr/bin/env python3
"""3-lru_cache
Implements LRU caching.
"""

from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """A class LRUCache that inherits from BaseCaching and
    is a caching system.
    """

    def __init__(self):
        """Initialize."""
        super().__init__()
        self.order = OrderedDict()

    def put(self, key, item):
        """Add an item to the cache."""
        if key is not None and item is not None:
            if key in self.cache_data:
                self.order.move_to_end(key)
            self.cache_data[key] = item
            self.order[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                least_used_item = self.order.popitem(last=False)
                del self.cache_data[least_used_item[0]]
                print(f"DISCARD: {least_used_item[0]}")

    def get(self, key):
        """Get an item by key."""
        if key is not None and key in self.cache_data:
            self.order.move_to_end(key)
            return self.cache_data[key]
        return None
