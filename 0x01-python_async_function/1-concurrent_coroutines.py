#!/usr/bin/env python3
"""
A module that execute multiple coroutines at the same time with async
"""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """
    A method that return the list of all the delays (float values)
    in ascending order without using sort.
    """
    delays = [wait_random(max_delay) for w in range(n)]
    complete = []
    for task in asyncio.as_completed(delays):
        complete.append(await task)
    return complete
