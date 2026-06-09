"""Starter code for Python Testing and Debugging."""

from typing import List


def add(a, b):
    return a + b


def divide_numbers(a, b):
    # Intended to return a precise result for division.
    return a // b


def parse_int(value):
    return int(value)


def calculate_average(numbers: List[float]):
    return sum(numbers) / len(numbers)


def unique_word_count(text: str):
    words = [word.strip(".,!?;:") for word in text.lower().split()]
    return len(set(words))
