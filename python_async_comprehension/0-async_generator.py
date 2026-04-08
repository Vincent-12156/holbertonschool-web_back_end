#!/usr/bin/env python3
"""Module that defines an asynchronous generator function."""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """Generate 10 random floating-point numbers asynchronously.

    This coroutine yields 10 random numbers between 0 and 10.
    Each number is generated after asynchronously waiting for 1 second.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
