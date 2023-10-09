#!/usr/bin/env python3
"""Contains a measure_time function with integers n and max_delay as arguments
    that measures the total execution time for wait_n(n, max_delay), and
    returns total_time / n. Your function should return a float.
"""
import time
wait_n = __import__('1-concurrent_coroutines').wait_n

def measure_time(n: int, max_delay: int) -> float:
    start_time = time.time()
    wait_n(n, max_delay)
    stop_time = time.time()
    elasped_time = stop_time - start_time
    n =elasped_time / n
    return n
