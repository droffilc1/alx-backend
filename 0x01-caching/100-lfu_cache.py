#!/usr/bin/env python3
"""100-lfu_cache
Implements LFU caching.
"""

from collections import defaultdict
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """A class LFUCache that inherits from BaseCaching and
    is a caching system.
    """

    def __init__(self):
        """Initialize."""
        super().__init__()
        self.freq = defaultdict(int)
        self.usage_order = defaultdict(list)

    def put(self, key, item):
        """Add an item to the cache."""
        if key is None and item is None:
            return
        if key in self.cache_data:
            self.freq[key] += 1
            self.cache_data[key] = item
            # Tracks usage order to resolve ties in LFU
            self.usage_order[self.freq[key]].append(key)
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                lfu_key = min(self.freq, key=self.freq.get)
                lfu_freq = self.freq[lfu_key]
                # To handle the case where multiple keys have the same
                # frequency
                for k in self.usage_order[lfu_freq]:
                    if k == lfu_key:
                        self.usage_order[lfu_freq].remove(k)
                        break

                print(f"DISCARD: {lfu_key}")
                del self.cache_data[lfu_key]
                del self.freq[lfu_key]
            self.cache_data[key] = item
            self.freq[key] += 1
            self.usage_order[self.freq[key]].append(key)

    def get(self, key):
        """Get an item by key."""
        if key is None or key not in self.cache_data:
            return None

        self.freq[key] += 1
        self.usage_order[self.freq[key]].append(key)
        return self.cache_data[key]
