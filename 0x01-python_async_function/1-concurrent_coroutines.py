#!/usr/bin/env python3
""" function that returns ana async ran delay"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ spawn wait_random n times with the specified
    max_delay."""
    tasks = []
    for i in range(n):
        waittimes = asyncio.create_task(wait_random(max_delay))
        tasks.append(waittimes)
    return [await task for task in asyncio.as_completed(tasks)]
