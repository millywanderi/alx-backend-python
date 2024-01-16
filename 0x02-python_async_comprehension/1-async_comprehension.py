#!/usr/bin/env python3
"""
A coroutine called async_comprehension that takes no arguments.
"""
import asyncio
import random
from typing import Generator

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> Generator[float, None, None]:
    """Async Comprehension"""
    return [i async for i in async_generator()]
