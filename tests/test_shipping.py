# tests/test_shipping.py
import pytest
from logistics.shipping import calculate_shipping_cost

def test_normal():
    assert calculate_shipping_cost(2.0, 3.5) == pytest.approx(7.0)

def test_zero_weight():
    assert calculate_shipping_cost(0.0, 5.0) == pytest.approx(0.0)

def test_negative_weight():
    with pytest.raises(ValueError):
        calculate_shipping_cost(-1.0, 1.0)

def test_negative_rate():
    with pytest.raises(ValueError):
        calculate_shipping_cost(1.0, -1.0)

def test_invalid_types():
    with pytest.raises(ValueError):
        calculate_shipping_cost("a", 1.0)