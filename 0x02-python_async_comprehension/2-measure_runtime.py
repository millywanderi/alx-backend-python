#!/usr/bin/env python3
"""
A module that run time for four parallel comprehensions
"""
from time import time
from typing import List
from asyncio import gather

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    measure_runtime coroutine that will execute async_comprehension four times
    in parallel using asyncio.gather
    """
    start_time = time()
    await gather(async_comprehension(), async_comprehension(),
                 async_comprehension(), async_comprehension())
    stop_time = time()
    return stop_time - start_time
