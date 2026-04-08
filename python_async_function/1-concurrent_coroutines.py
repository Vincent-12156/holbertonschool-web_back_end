#!/usr/bin/env python3
"""
Module that executes multiple wait_random coroutines concurrently
and returns their results.
"""

import asyncio
from typing import List
import importlib


wait_random = importlib.import_module('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn wait_random n times with the specified max_delay
    and return a list of delays in ascending order.
    """
    coroutines = [wait_random(max_delay) for _ in range(n)]
    results = await asyncio.gather(*coroutines)

    return results
