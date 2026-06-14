#!/usr/bin/env python3
"""Module for measuring runtime."""
import asyncio
import time

wait_n = __import__('1-async_comprehension').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measure the total execution time for wait_n and return average."""
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n
