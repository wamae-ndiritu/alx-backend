#!/usr/bin/env python3
"""
Defines a simple helper function
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Return a tuple of start index and end index for pagination.

    Args:
        page (int): The page number (1-indexed).
        page_size (int): The size of each page.

    Returns:
        tuple[int, int]: The start index and end
        index for the given page and page size.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index
