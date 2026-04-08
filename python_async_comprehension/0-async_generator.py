#!/usr/bin/env python3
"""Module that defines an asynchronous generator function."""

import asyncio
import random


async def async_generator():
    """
    Asynchronous generator yielding 10 random numbers with 1s delay
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
