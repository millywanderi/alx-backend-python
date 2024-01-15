#!/usr/bin/env python3
"""
A module that execute multiple coroutines at the same time with async
"""

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list:
    """
    A method that return the list of all the delays (float values)
    in ascending order without using sort.
    """
    delays = [asyncio.create_task(wait_random(max_delay))for _ in range(n)]
    return [await delay for delay in asyncio.as_completed(delays)]
