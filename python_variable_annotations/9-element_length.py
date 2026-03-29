#!/usr/bin/env python3
"""
Annotated function that returns list of tuples with els & lengths.
"""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Takes an iterable seqs and returns list of tups
    """
    return [(i, len(i)) for i in lst]
