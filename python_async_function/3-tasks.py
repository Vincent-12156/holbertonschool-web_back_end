#!/usr/bin/env python3
"""Module that creates an asyncio Task from the wait_random coroutine."""

import asyncio
import importlib
from typing import Any


wait_random = importlib.import_module('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create and return an asyncio.Task that runs wait_random(max_delay).
    """
    return asyncio.create_task(wait_random(max_delay))
