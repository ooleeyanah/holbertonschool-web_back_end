#!/usr/bin/env python3
"""
Task-based version of wait_n
"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn task_wait_random n times with specified max_delay

    """
    delays = []

    # Create all tasks using task_wait_random
    tasks = [task_wait_random(max_delay) for _ in range(n)]

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
