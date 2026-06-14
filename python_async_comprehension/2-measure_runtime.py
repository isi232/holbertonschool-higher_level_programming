#!/usr/bin/env python3
"""Task 2: Measure execution time of async functions"""

import asyncio
import time
from typing import List
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Method to measure average run time of wait_n"""
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    stop = time.time()
    return (stop - start) / n
