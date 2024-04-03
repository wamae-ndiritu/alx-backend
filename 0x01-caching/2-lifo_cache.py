#!/usr/bin/env python3
"""
LIFO Caching
"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """
    Implements Caching using the LIFO
    replacement algorithm
    """
    def __init__(self):
        """
        Instantiates the class
        """
        super().__init__()

    def put(self, key, item):
        """
        Adds items to the cache
        If the cache is full then it discards
        the last item that was added
        """
        if key and item:
            cache_items_count = len([key for key in self.cache_data.keys()])

            if cache_items_count >= BaseCaching.MAX_ITEMS:
                # Removes the last added key
                last_added = self.cache_data.popitem()
                print(f"DISCARD: {last_added[0]}")
            self.cache_data[key] = item

    def get(self, key):
        """
        Gets cache items
        """
        if key is None:
            return None
        try:
            cache_items = self.cache_data[key]
            return cache_items
        except KeyError:
            return None
