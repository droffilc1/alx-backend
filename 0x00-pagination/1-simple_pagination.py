#!/usr/bin/env python3
""" 1-simple_pagination """

import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """Simple helper function.

    Args:
        page: pages
        page_size: page size

    Returns a tuple of size two containing a start index and an end index
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)


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
        """Gets the page"""
        dataset = self.dataset()
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0
        indices = index_range(page, page_size)
        start_index = indices[0]
        end_index = indices[1]
        if start_index >= len(dataset) or end_index < 0:
            return []
        return dataset[start_index:end_index]
