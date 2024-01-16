#!/usr/bin/env python3
"""
A coroutine called async_generator that takes no arguments.
"""

import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Async Generator"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
