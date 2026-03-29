#!/usr/bin/env python3


"""
Define function that takes str and int/float & returns tuple

"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Return tuple from str & int/float
    """
    return (k, float(v * v))
