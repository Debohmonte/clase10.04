import pytest
from calculadora import sumar, restar, multiplicar, dividir

def test_sumar():
    assert sumar(2, 3) == 5
    assert sumar(-1, 1) == 0

def test_restar():
    assert restar(5, 2) == 3
    assert restar(10, 5) == 5

def test_multiplicar():
    assert multiplicar(2, 3) == 6
    assert multiplicar(5, 0) == 0

def test_dividir():
    assert dividir(6, 2) == 3
    with pytest.raises(ValueError):
        dividir(5, 0)
