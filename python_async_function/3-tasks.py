#!/usr/bin/env python3
"""
Task function for wait_random
"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Reg function that takes int max_delay and returns asyncio.Task

    """
    return asyncio.create_task(wait_random(max_delay))
