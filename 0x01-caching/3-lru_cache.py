#!/usr/bin/env python3
"""
LRU Caching
"""
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """
    Implements Caching using the LRU
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
        the least recently used item
        """
        if key and item:
            cache_items_count = len([key for key in self.cache_data.keys()])

            if cache_items_count >= BaseCaching.MAX_ITEMS:
                # top in the ordered dict is the LRU
                top_item = next(iter(self.cache_data))
                self.cache_data.pop(top_item)
                print(f"DISCARD: {top_item}")
            self.cache_data[key] = item

    def get(self, key):
        """
        Gets cache items
        """
        if key is None:
            return None
        try:
            cache_item = self.cache_data[key]
            # Move the item to the end of the dict
            self.cache_data[key] = cache_item
            return cache_item
        except KeyError:
            return None
