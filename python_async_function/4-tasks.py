#!/usr/bin/env python3
"""Async module with task_wait_n using task_wait_random"""

import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Run task_wait_random n times concurrently
    and return list of delays in order
    """
    tasks = [
        asyncio.create_task(task_wait_random(max_delay))
        for _ in range(n)
    ]

    results = await asyncio.gather(*tasks)
    return results