#!/usr/bin/env python3


"""
Define function that takes str and int/float & returns tuple

"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Creates function that multi float by given multiplier
    """
    def multiplier_function(x: float) -> float:
        return x * multiplier
    return multiplier_function
