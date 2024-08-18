#!/usr/bin/env python3
"""
    Defines the class Server that paginates a database of popular baby names.
"""
import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """
        Returns a tuple that contains the start index and end index of
        data to be returned for a particular pagination parameters.
    """
    return ((page - 1) * page_size, page * page_size)


class Server:
    """
        Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """ Cached dataset. """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ Returns a range of data from the dataset. """
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0
        start_index, end_index = index_range(page, page_size)

        if self.__dataset is None:
            data = self.dataset()
        else:
            data = self.__dataset

        return data[start_index:end_index]
