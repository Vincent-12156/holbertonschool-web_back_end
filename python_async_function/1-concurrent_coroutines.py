#!/usr/bin/env python3
"""
Module to run multiple wait_random coroutines concurrently
"""

import asyncio
from random import uniform


async def wait_random(max_delay: int = 10) -> float:
    """Waits for a random delay between 0 and max_delay seconds."""
    delay = uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


async def wait_n(n: int, max_delay: int) -> list[float]:
    """
    Spawn wait_random n times with max_delay.
    Returns list of delays in the order they completed
    (ascending by completion time)
    """
    coroutines = [wait_random(max_delay) for _ in range(n)]
    delays = []

    for coro in asyncio.as_completed(coroutines):
        result = await coro
        delays.append(result)

    return delays
