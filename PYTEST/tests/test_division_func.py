from my_funcs.Pytest_1 import division
import pytest


@pytest.mark.parametrize("a, b , expected_result",
                         [(10, 2, 5), (20, 10, 2), (30, -3, -10), (5, 2, 2.5)])  # декоратор для 4 тестов
def test_division_good(a, b, expected_result):
    assert division(a, b) == expected_result  # функция assert проверяет истинность выражения


# def test_division_one_more():
#     assert division(10, 5) == 2
@pytest.mark.parametrize("expected_exception, divider, divisionable", [(ZeroDivisionError, 0, 10),
                                                         (TypeError, "2", 20)])
def test_division_with_error(expected_exception, divider, divisionable):
    with pytest.raises(expected_exception):
        division(divisionable, divider)


# def test_type_error():
#     with pytest.raises(TypeError):
#         division(10, "2")
