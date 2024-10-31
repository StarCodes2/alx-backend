#!/usr/bin/env python3
""" Defines class BasicCache that inherits from BaseCaching and impliments
    a caching system.
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ defines a simple caching system that add items to a cache and
        remove them by key.
    """
    def __init__(self):
        """ Initialise an object. """
        super().__init__()

    def put(self, key, item):
        """ Adds a new item to the cache. """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ Returns an item from the cache that matches a given key. """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
