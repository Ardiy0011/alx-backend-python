#!/usr/bin/env python3
""" function that returns an async random delay """

import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int = 0, max_delay: int = 0) -> float:
    """ measure the total execution time for wait_n"""
    start = time.perf_counter()
    await wait_n(n, max_delay)
    end = time.perf_counter()
    return (end - start) / n
