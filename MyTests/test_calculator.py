import pytest
from calculator import add, substract, multiply, divide


# Пример использования фикстуры для подготовки данных
@pytest.fixture
def prepare_data():
    data = {"x": 10, "y": 5}
    return data


def test_add(prepare_data):
    result = add(prepare_data["x"], prepare_data['y'])
    assert result == 15


def test_substract(prepare_data):
    result = substract(prepare_data['x'], prepare_data['y'])
    assert result == 5


def test_multiply(prepare_data):
    result = multiply(prepare_data['x'], prepare_data['y'])
    assert result == 50


# Пример использования параметризации
@pytest.mark.parametrize('x, y, expected', [(10, 2, 5), (20, 4, 5)])
def test_divide(x, y, expected):
    result = divide(x, y)
    assert result == expected


def test_divide_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)
