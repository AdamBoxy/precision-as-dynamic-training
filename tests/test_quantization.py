import torch
from lapa.quantization import fake_quantize_symmetric

def test_zero_stays_zero():
    x=torch.zeros(10); assert torch.equal(fake_quantize_symmetric(x,4),x)

def test_range_is_bounded():
    x=torch.tensor([-1.0,-0.25,0.0,0.4,1.0]); y=fake_quantize_symmetric(x,4)
    assert y.abs().max() <= x.abs().max()+1e-6

def test_more_bits_reduce_sample_error():
    x=torch.linspace(-1.0,1.0,101)
    e4=torch.mean((x-fake_quantize_symmetric(x,4))**2)
    e8=torch.mean((x-fake_quantize_symmetric(x,8))**2)
    assert e8 <= e4
