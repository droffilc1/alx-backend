#!/usr/bin/env python3
""" 2-hypermedia_pagination """

import csv
import math
from typing import List, Dict, Any


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

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """Implements hypermedia pagination.

        Args:
        page (int): The current page number. Defaults to 1.
        page_size (int): The number of items per page. Defaults to 10.

        Returns:
            Dict[str, Any]: A dictionary containing pagination information:
              page_size: the length of the returned dataset page
              page: the current page number
              data: the dataset page (equivalent to return from previous task)
              next_page: number of the next page, None if no next page
              prev_page: number of the previous page, None if no previous page
              total_pages: the total number of pages in the dataset as an
                integer
        """
        dataset = self.dataset()
        data = self.get_page(page, page_size)
        total_pages = math.ceil(len(dataset) / page_size)
        has_next_page = page < total_pages
        has_prev_page = page > 1
        return {
            "page_size": page_size,
            "page": page,
            "data": data,
            "next_page": page + 1 if has_next_page else None,
            "prev_page": page - 1 if has_prev_page else None,
            "total_pages": total_pages
        }
