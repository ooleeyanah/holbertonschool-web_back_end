#!/usr/bin/env python3
"""
Asynchronous coroutine wait_n
"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn wait_random n times with the specified max_delay.

    """
    delays = []

    # Create all coroutine tasks
    tasks = [wait_random(max_delay) for _ in range(n)]

    # Get results as they complete and insert in sorted order
    for coro in asyncio.as_completed(tasks):
        delay = await coro
        # Insert delay in correct position to maintain ascending order
        inserted = False
        for i, existing_delay in enumerate(delays):
            if delay < existing_delay:
                delays.insert(i, delay)
                inserted = True
                break
        if not inserted:
            delays.append(delay)

    return delays
