#!/usr/bin/env python3
"""
Coroutine that collects 10 random numbers from async_generator.
"""
from typing import List

async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """
    Collect 10 random numbers using an async comprehension.
    """
    return [value async for value in async_generator()]
