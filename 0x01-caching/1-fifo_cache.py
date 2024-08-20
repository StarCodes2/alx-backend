#!/usr/bin/env python3
""" Defines class FIFOCache that inherits from BaseCaching and impliments
    a first in first out caching system
"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """ defines a simple caching system of a fixed size that add items to a
        cache using FIFO and remove them by key
    """
    def __init__(self):
        """ Initialise an object. """
        super().__init__()

    def put(self, key, item):
        """ Adds a new item to the cache. """
        if key is not None and item is not None:
            if BaseCaching.MAX_ITEMS <= len(self.cache_data):
                rKey = next(iter(self.cache_data))
                del self.cache_data[rKey]
                print("DISCARD: {}".format(rKey))
            self.cache_data[key] = item

    def get(self, key):
        """ Returns an item from the cache that matches a given key. """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
