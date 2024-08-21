#!/usr/bin/env python3
""" Defines class MRUCache that inherits from BaseCaching and impliments
    a most recently used caching system.
"""
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """ defines a simple caching system of a fixed size that adding and
        removing items from the cache using MRU policy.
    """
    def __init__(self):
        """ Initialise an object. """
        self._count = 0
        self._rUsed = {}
        super().__init__()

    def put(self, key, item):
        """ Adds a new item to the cache. """
        if key is not None and item is not None:
            if BaseCaching.MAX_ITEMS <= len(self.cache_data) and\
               key not in self.cache_data:
                rValue = max(self._rUsed.values())
                rKey = ""
                for k, v in self._rUsed.items():
                    if rValue == v:
                        rKey = k
                self.cache_data.pop(rKey)
                self._rUsed.pop(rKey)
                print("DISCARD: {}".format(rKey))

            self.cache_data[key] = item
            self._rUsed[key] = self._count
            self._count += 1

    def get(self, key):
        """ Returns an item from the cache that matches a given key. """
        if key is not None and key in self.cache_data:
            self._rUsed[key] = self._count
            self._count += 1
            return self.cache_data[key]
        return None
