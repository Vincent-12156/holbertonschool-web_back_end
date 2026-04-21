#!/usr/bin/env python3
"""
Module that provides a helper function for pagination calculations
"""


def index_range(page: int, page_size: int) -> tuple[int, int]:
    """
    Return the start and end index for a given page and page size
    """
    start: int = (page - 1) * page_size
    end: int = page * page_size
    return (start, end)
