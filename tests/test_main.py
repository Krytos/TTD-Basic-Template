import pytest

from tdd.main import simple_add, simple_div, simple_i_o


@pytest.mark.parametrize("test_input, expected", [("hello", "hello"), ("world", "world")])
def test_simple_i_o(test_input, expected):
    assert simple_i_o(test_input) == expected


@pytest.mark.parametrize("test_input_1, test_input_2, expected",
                         [(1, 2, 3), (2, 3, 5), (3, 4, 7), (4, 5, 9), (5, 6, 11)]
                         )
def test_simple_add(test_input_1, test_input_2, expected):
    assert simple_add(test_input_1, test_input_2) == expected


@pytest.mark.parametrize("test_input_1, test_input_2, expected",
                         [(1, 2, 0.5), (2, 3, 0.6666666666666666), (3, 4, 0.75), (4, 5, 0.8),
                          (5, 6, 0.8333333333333334)]
                         )
def test_simple_div(test_input_1, test_input_2, expected):
    assert simple_div(test_input_1, test_input_2) == expected
    with pytest.raises(ZeroDivisionError):
        simple_div(1, 0)
