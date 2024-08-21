#!/usr/bin/env python3
""" Defines class MRUCache that inherits from BaseCaching and impliments
    a least frequently used caching system.
"""
from collections import defaultdict

BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """ defines a simple caching system of a fixed size that adding and
        removing items from the cache using LFU policy.
    """
    def __init__(self):
        """ Initialise an object. """
        self._rUsed = {}
        super().__init__()

    def put(self, key, item):
        """ Adds a new item to the cache. """
        if key is not None and item is not None:
            if BaseCaching.MAX_ITEMS <= len(self.cache_data) and\
               key not in self.cache_data:
                rValue = min(self._rUsed.values())
                rKey = ""
                for k, v in self._rUsed.items():
                    if rValue == v:
                        rKey = k
                        break
                self.cache_data.pop(rKey)
                self._rUsed.pop(rKey)
                print("DISCARD: {}".format(rKey))

            self.cache_data[key] = item
            if key in self._rUsed:
                self._rUsed[key] += 1
            else:
                self._rUsed[key] = 1

    def get(self, key):
        """ Returns an item from the cache that matches a given key. """
        if key is not None and key in self.cache_data:
            self._rUsed[key] += 1
            return self.cache_data[key]
        return None
