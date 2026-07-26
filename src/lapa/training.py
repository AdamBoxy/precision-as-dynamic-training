"""Training helpers for the demonstration experiment."""
import torch
from torch import nn
from .quantization import fake_quantize_symmetric

def gradient_activity(model: nn.Module) -> float:
    values = [p.grad.detach().abs().mean() for p in model.parameters() if p.grad is not None]
    return float(torch.stack(values).mean().item()) if values else 0.0

@torch.no_grad()
def apply_fake_quantization(model: nn.Module, bits: int) -> None:
    for parameter in model.parameters():
        parameter.copy_(fake_quantize_symmetric(parameter, bits))

@torch.no_grad()
def accuracy(model, inputs, targets) -> float:
    return float((model(inputs).argmax(dim=1) == targets).float().mean().item())

def train_epoch(model, optimizer, criterion, inputs, targets, controller=None, static_bits=None):
    model.train(); optimizer.zero_grad(set_to_none=True)
    loss = criterion(model(inputs), targets); loss.backward()
    activity = gradient_activity(model); optimizer.step()
    bits = controller.allocate(activity).bits if controller else static_bits or 32
    if bits != 32:
        apply_fake_quantization(model, bits)
    return float(loss.item()), activity, bits
