#!/usr/bin/env python3
"""
The coroutine will collect 10 random numbers using an async comprehensing over
async_generator, then return the 10 random numbers.
"""
import asyncio
async_generator = __import__('0-async_generator').async_generator
from typing import Generator, List

async def async_comprehension() -> List[Generator[float, None, None]]:
    """refer to the above comment"""
    return [i async for i in async_generator()]
