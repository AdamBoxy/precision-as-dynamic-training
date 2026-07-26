"""Metrics for adaptive-precision experiments."""
from collections import Counter

def effective_bits(bit_widths):
    values = list(bit_widths)
    if not values:
        raise ValueError("at least one bit width is required")
    return sum(values) / len(values)

def precision_histogram(bit_widths):
    return dict(sorted(Counter(bit_widths).items()))
