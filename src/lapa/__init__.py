"""Learning-Activity Precision Allocation (LAPA)."""
from .controller import LAPAController, PrecisionDecision
from .quantization import fake_quantize_symmetric
__all__ = ["LAPAController", "PrecisionDecision", "fake_quantize_symmetric"]
__version__ = "0.1.0"
