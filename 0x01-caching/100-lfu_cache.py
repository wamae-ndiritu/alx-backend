#!/usr/bin/env python3
"""
LFU Caching
"""
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """
    Implements Caching using the LFU
    replacement algorithm
    """
    def __init__(self):
        """
        Instantiates the class
        """
        super().__init__()
        self.cache_frequency = {}

    def put(self, key, item):
        """
        Adds items to the cache
        If the cache is full then it discards
        the least frequently used item
        """
        if key and item:
            cache_items_count = len([key for key in self.cache_data.keys()])

            if key in self.cache_data:
                self.cache_frequency[key] += 1
            else:
                self.cache_frequency[key] = 1
            if cache_items_count >= BaseCaching.MAX_ITEMS:
                frequencies = [value for value in (
                        self.cache_frequency.values()
                        )]
                least_frequency = min(frequencies)
                for k, value in self.cache_frequency.items():
                    if value == least_frequency:
                        if k in self.cache_data.keys():
                            self.cache_data.pop(k)
                            self.cache_frequency.pop(k)
                            print(f"DISCARD: {k}")
                        break
            self.cache_data[key] = item

    def get(self, key):
        """
        Gets cache items
        """
        if key is None:
            return None
        try:
            cache_item = self.cache_data[key]
            # Update cache frequency
            self.cache_frequency[key] += 1
            return cache_item
        except KeyError:
            return None
