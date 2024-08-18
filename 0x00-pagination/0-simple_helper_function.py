#!/usr/bin/env python3
"""
    Defines a function named index_range that takes two integer arguments
    page and page_size.
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """
        Returns a tuple that contains the start index and end index of
        data to be returned for a particular pagination parameters.
    """
    return ((page - 1) * page_size, page * page_size)
