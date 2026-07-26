"""Precision allocation controller."""
from dataclasses import dataclass
from typing import Iterable

@dataclass(frozen=True)
class PrecisionDecision:
    activity: float
    bits: int

class LAPAController:
    """Map a non-negative activity signal to a permitted bit width."""
    def __init__(self, thresholds=(0.01, 0.05), bit_widths=(4, 8, 16)):
        low, high = thresholds
        if low < 0 or high <= low:
            raise ValueError("thresholds must satisfy 0 <= low < high")
        if len(bit_widths) != 3 or any(bits < 2 for bits in bit_widths):
            raise ValueError("bit_widths must contain three values of at least 2 bits")
        self.thresholds = thresholds
        self.bit_widths = bit_widths

    def allocate(self, activity: float) -> PrecisionDecision:
        if activity < 0:
            raise ValueError("activity must be non-negative")
        low, high = self.thresholds
        low_bits, mid_bits, high_bits = self.bit_widths
        bits = low_bits if activity < low else mid_bits if activity < high else high_bits
        return PrecisionDecision(float(activity), bits)

    def allocate_many(self, activities: Iterable[float]):
        return [self.allocate(value) for value in activities]

    @staticmethod
    def effective_bits(decisions):
        decisions = list(decisions)
        if not decisions:
            raise ValueError("at least one decision is required")
        return sum(item.bits for item in decisions) / len(decisions)
