#!/usr/bin/env python3
"""
    Desription: Import async_comprehension from the previous file and write a
                measure_runtime coroutine that will execute async_comprehension
                four times in parallel using asyncio.gather.

                measure_runtime should measure the total runtime and return it.
                Notice that the total runtime is roughly 10 seconds, explain
                it to yourself.
"""

import asyncio
from time import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ Measure the runtime of async_comprehension executed 4 times in
        parallel. """
    start_time = time()
    tasks = [async_comprehension() for i in range(4)]
    await asyncio.gather(*tasks)
    end_time = time()

    return end_time - start_time
