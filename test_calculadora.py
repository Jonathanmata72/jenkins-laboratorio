import pytest
from calculadora import calcular_descuento

def test_descuento_10():
    assert calcular_descuento(100000, 10) == 90000

def test_descuento_50():
    assert calcular_descuento(200000, 50) == 100000

def test_sin_descuento():
    assert calcular_descuento(50000, 0) == 50000

def test_descuento_invalido():
    with pytest.raises(ValueError):
        calcular_descuento(100000, 120)

def test_precio_negativo():
    with pytest.raises(ValueError):
        calcular_descuento(-1000, 10)
