#!/usr/bin/env python3
"""Async comprehension."""

async_generator = __import__("0-async_generator").async_generator


async def async_comprehension():
    """Collect 10 random numbers from async_generator."""
    return [number async for number in async_generator()]
