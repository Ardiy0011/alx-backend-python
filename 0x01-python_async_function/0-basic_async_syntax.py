#!/usr/bin/env python3
""" function that returns ana async ran delay"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    waits for a random delay between 0 and max_delay (included and float value)
    seconds and eventually returns.
    """
    random_del = random.uniform(0, max_delay)
    await asyncio.sleep(random_del)
    return random_del
