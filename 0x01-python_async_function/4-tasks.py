#!/usr/bin/env python3
"""
A module that executes multiple coroutines at the same time with async.
"""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """spawn task_wait_random n times with the specified max_delay"""
    tasks = [task_wait_random(max_delay) for w in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]
