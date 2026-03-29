#!/usr/bin/env python3


"""
Defining a function that calculates sum of list of int and float.

"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Calculates sum of list of floats and ints.
    """
    return float(sum(mxd_lst))
