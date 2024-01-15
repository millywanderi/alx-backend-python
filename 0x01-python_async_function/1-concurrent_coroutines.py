#!/usr/bin/env python3
"""
A module that execute multiple coroutines at the same time with async
"""

import asyncio
import typing
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> typing.List:
    """
    A method that return the list of all the delays (float values)
    in ascending order without using sort.
    """
    list_delays = []
    for w in range(n):
        delays = await wait_random(max_delay)
        list_delays.append(delays)
    return sorted(list_delays)
