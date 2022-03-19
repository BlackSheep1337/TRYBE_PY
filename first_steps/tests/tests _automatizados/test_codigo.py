import pytest
from codigo import is_even, divide


def test_is_even_when_number_is_even_return_true():
    'Para um número par a função deve retornar o valor True'
    assert is_even(2) is True

def test_is_even_when_number_is_not_even_return_false():
    'Para um número ímpar a função deve retornar o valor False'
    assert is_even(3) is False

def test_divide_when_other_number_is_zero_raises_exception():
    with pytest.raises(ZeroDivisionError, match="division by zero"):
        divide(10, 0)