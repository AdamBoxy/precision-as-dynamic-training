"""Deterministic fake-quantization helpers."""
import torch
from torch import Tensor

def fake_quantize_symmetric(tensor: Tensor, bits: int, eps: float = 1e-12) -> Tensor:
    """Simulate signed symmetric uniform quantization in floating point."""
    if bits < 2:
        raise ValueError("bits must be at least 2")
    if tensor.numel() == 0:
        return tensor.clone()
    qmax = (2 ** (bits - 1)) - 1
    max_abs = tensor.detach().abs().max()
    if max_abs <= eps:
        return tensor.clone()
    scale = max_abs / qmax
    return torch.clamp(torch.round(tensor / scale), -qmax, qmax) * scale
