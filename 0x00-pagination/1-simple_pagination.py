#!/usr/bin/env python3
"""
Simple pagination
"""
import csv
from typing import List, Tuple


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
    assert isinstance(page, int) and page > 0, (
            "Page must be an integer greater than 0"
    )
    assert isinstance(page_size, int) and page_size > 0, (
            "Page size must be an integer greater than 0"
    )

    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Get the specified page of the dataset.

        Args:
            page (int): The page number (1-indexed).
            page_size (int): The size of each page.

        Returns:
            List[List]: The data for the specified page.
        """
        start_index, end_index = index_range(page, page_size)
        dataset = self.dataset()
        return dataset[start_index:end_index]
