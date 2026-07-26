import pytest
from lapa.controller import LAPAController

def test_allocations():
    c=LAPAController((0.1,0.5),(4,8,16))
    assert [c.allocate(x).bits for x in (0.0,0.1,0.49,0.5)] == [4,8,8,16]

def test_effective_bits():
    c=LAPAController((0.1,0.5),(4,8,16))
    assert c.effective_bits(c.allocate_many([0.0,0.2,1.0])) == pytest.approx(28/3)

def test_negative_rejected():
    with pytest.raises(ValueError): LAPAController().allocate(-0.01)
