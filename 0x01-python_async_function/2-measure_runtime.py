#!/usr/bin/env python3
"""Contains a measure_time function with integers n and max_delay as arguments
    that measures the total execution time for wait_n(n, max_delay), and
    returns total_time / n. Your function should return a float.
"""
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Contains a measure_time function with integers n and max_delay as arguments
        that measures the total execution time for wait_n(n, max_delay), and
        returns total_time / n. Your function should return a float.
    """
    start_time: float = time.time()
    asyncio.run(wait_n(n, max_delay))
    elasped_time: float = time.time() - start_time
    return elasped_time / n
