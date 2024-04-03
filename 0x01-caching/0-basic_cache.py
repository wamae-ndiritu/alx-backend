#!/usr/bin/env python3
"""
Basic dictionary
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    Caching system
    """

    def put(self, key, item):
        """
        Add a key-value pair in the cache_data
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """
        Get the cache item with the specified key
        in a cache system
        """
        if key is None:
            return None
        keyFound = False
        for item in self.cache_data.keys():
            if item == key:
                keyFound = True
                break
        if not keyFound:
            return None
        return self.cache_data[key]
