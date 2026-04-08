#!/usr/bin/env python3
"""Module that defines a coroutine for collecting random numbers."""

from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Collect 10 random numbers using an async comprehension.

    This coroutine uses an asynchronous comprehension to retrieve
    10 random floating-point numbers from async_generator and
    returns them as a list.
    """
    return [number async for number in async_generator()]
