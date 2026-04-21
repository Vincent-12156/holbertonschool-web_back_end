#!/usr/bin/env python3
"""
Module that provides hypermedia pagination for a CSV dataset.
"""

import csv
import math
from typing import List, Tuple, Dict, Optional


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Return a tuple containing the start index and end index
    """
    start: int = (page - 1) * page_size
    end: int = page * page_size
    return (start, end)


class Server:
    """
    Server class to paginate a database of popular baby names.
    """

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initialize server with no cached dataset."""
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Load and cache dataset from CSV file
        and return a list of dataset rows excluding header.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Return a page of the dataset based on pagination parameters.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start, end = index_range(page, page_size)
        data = self.dataset()

        if start >= len(data):
            return []

        return data[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        Return hypermedia pagination information for the dataset.
        """
        data = self.get_page(page, page_size)
        total_items = len(data)
        total_pages = math.ceil(total_items / page_size)

        if page == 1:
            prev_page = None
        else:
            prev_page = page - 1

        if page == total_pages:
            next_page = None
        else:
            next_page = page + 1

        dict = {
            "page_size": page_size,
            "page": page, "data": data,
            "next_page": next_page, "prev_page": prev_page,
            "total_pages": total_pages
        }

        return dict
