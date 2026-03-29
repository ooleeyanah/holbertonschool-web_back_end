#!/usr/bin/env python3


"""
Defining different variables of varying types to show type annotation.

"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Calculates sum of list of floats.
    """
    return sum(input_list)
