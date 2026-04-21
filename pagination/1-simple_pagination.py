#!/usr/bin/env python3
"""
Module that provides simple pagination utilities for a CSV dataset.
"""

import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    A tuple containing the start index and end index
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
        """Initialize the server with no cached dataset."""
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Return the cached dataset, loading it from the CSV file if needed.

        Returns:
            A list of rows from the dataset (excluding the header).
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

        Args:
            page: The page number (1-indexed).
            page_size: The number of items per page.

        Returns:
            A list of rows corresponding to the requested page.

        Raises:
            AssertionError: If page or page_size are not positive integers.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start, end = index_range(page, page_size)
        data = self.dataset()

        if start >= len(data):
            return []

        return data[start:end]
