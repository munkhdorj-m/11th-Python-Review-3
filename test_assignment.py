import pytest
import inspect
from assignment import factorial, is_prime, max_min, second_largest, count_pos_neg_zero

def check_contains_loop(function):
    source = inspect.getsource(function)
    return 'for' in source or 'while' in source


# Exercise 1: Factorial using loop
@pytest.mark.parametrize("n, expected", [
    (5, 120),
    (0, 1),
    (7, 5040),
    (3, 6),
    (1, 1)
])
def test1(n, expected):
    assert factorial(n) == expected
    assert check_contains_loop(factorial)


# Exercise 2: Prime check using loop
@pytest.mark.parametrize("n, expected", [
    (7, True),
    (12, False),
    (1, False),
    (2, True),
    (29, True),
    (30, False)
])
def test2(n, expected):
    assert is_prime(n) == expected
    assert check_contains_loop(is_prime)


# Exercise 3: Max and Min in a list using loop
@pytest.mark.parametrize("lst, expected", [
    ([3, 7, 2, 9, 5], [9, 2]),
    ([10, -4, 0, 8], [10, -4]),
    ([1, 1, 1, 1], [1, 1]),
    ([-5, -2, -9, -1], [-1, -9])
])
def test3(lst, expected):
    assert max_min(lst) == expected
    assert check_contains_loop(max_min)


# Exercise 4: Second largest number using loop
@pytest.mark.parametrize("lst, expected", [
    ([3, 7, 2, 9, 5], 7),
    ([10, 10, 8, 5], 10),
    ([1, 2, 3, 4, 5], 4),
    ([5, 5, 5], 5)
])
def test4(lst, expected):
    assert second_largest(lst) == expected
    assert check_contains_loop(second_largest)


# Exercise 5: Count positive, negative, zero using loop
@pytest.mark.parametrize("lst, expected", [
    ([3, -2, 0, 5, -1], [2, 2, 1]),
    ([0, 0, 0], [0, 0, 3]),
    ([-5, 2, 7, -1, 0, 0], [2, 2, 2]),
    ([1, -1, 2, -2, 0], [2, 2, 1])
])
def test5(lst, expected):
    assert count_pos_neg_zero(lst) == expected
    assert check_contains_loop(count_pos_neg_zero)
