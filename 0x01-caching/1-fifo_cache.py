#!/usr/bin/env python3
"""
FIFO Caching
"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
    Implements Caching using the FIFO
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
        the first item that was added
        """
        if key and item:
            cache_items_count = len([key for key in self.cache_data.keys()])
            
            if cache_items_count == BaseCaching.MAX_ITEMS:
                first_key = next(iter(self.cache_data)) # Get the first key
                self.cache_data.pop(first_key)
                print(f"DISCARD: {first_key}")
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
