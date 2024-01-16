from testing.division import fun
import pytest


@pytest.mark.parametrize("a, b, result", [(10, 2, 5),
                                          (20, 10, 2),
                                          (30, -3, -10),
                                          (5, 2, 2.5)])
def test_fun_good(a, b, result):
    assert fun(a, b) == result


@pytest.mark.parametrize('result, param, division', [(ZeroDivisionError, 0, 10),
                                                     (TypeError, "2", 20)])
def test_with_error(result, param, division):
    with pytest.raises(result):
        assert fun(division, param)
