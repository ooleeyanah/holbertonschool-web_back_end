#!/usr/bin/env python3
"""
A coroutine that loops 10 times with async wait 1 sec to yield random int.
"""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Async coroutine that loops 10 times, waits 1 second
    and yields a random number between 0 and 10.

    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
