#!/usr/bin/env python3
"""
This module measures the runtime of the wait_n function.
"""

import asyncio
import time
from typing import List

# Import wait_n from the module with leading digit
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the average time taken by wait_n function.

    Args:
        n (int): The number of delays to wait for.
        max_delay (int): The maximum delay in seconds.

    Returns:
        float: The average time per call to wait_n.
    """
    start_time = time.time()  # Record the start time

    # Run the asyncio event loop to execute wait_n
    asyncio.run(wait_n(n, max_delay))

    total_time = time.time() - start_time  # Calculate the total time taken

    return total_time / n  # Return average time per call
