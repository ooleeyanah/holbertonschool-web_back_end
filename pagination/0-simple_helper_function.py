#!/usr/bin/env python3
"""Simple pagination helper function"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Return the start and end index for a given page and page size
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)
