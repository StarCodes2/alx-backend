#!/usr/bin/env python3
""" Defines class LIFOCache that inherits from BaseCaching and impliments
    a last in first out caching system.
"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """ defines a simple caching system of a fixed size that adding and
        removing items from the cache using the LIFO caching policy.
    """
    def __init__(self):
        """ Initialise an object. """
        self._lastIN = ""
        super().__init__()

    def put(self, key, item):
        """ Adds a new item to the cache. """
        if key is not None and item is not None:
            if BaseCaching.MAX_ITEMS <= len(self.cache_data) and\
               key not in self.cache_data:
                self.cache_data.pop(self._lastIN)
                print("DISCARD: {}".format(self._lastIN))
            self.cache_data[key] = item
            self._lastIN = key

    def get(self, key):
        """ Returns an item from the cache that matches a given key. """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
