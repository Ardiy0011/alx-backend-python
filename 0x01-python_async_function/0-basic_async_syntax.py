#!/usr/bin/env python3
""" function that returns ana async ran delay"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    random_del = random.uniform(0, max_delay)
    await asyncio.sleep(random_del)
    return random_del
