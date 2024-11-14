import pytest
import inspect
from assignment import index_of_highest_number, find_all_indices, swap_even_odd_indices

def check_contains_loop(function):
    source = inspect.getsource(function)
    return 'for' in source or 'while' in source

@pytest.mark.parametrize("numbers, expected", [
    ([3, 8, 2, 5, 10, 7], 4),
    ([12, 23, 43, 11, 9], 2),
    ([113, 234, 145, 299, 155], 3),
    ([5], 0),
    ([3, 3, 3], 0),
    ([-10, -5, -30], 1),
    ([0, -1, 2, -3], 2)
])
def test1(numbers, expected):
    assert index_of_highest_number(numbers) == expected
    assert check_contains_loop(index_of_highest_number)

@pytest.mark.parametrize("numbers, target, expected", [
    ([3, 8, 3, 5, 3, 7], 3, [0, 2, 4]),
    ([12, 23, 43, 11, 23], 23, [1, 4]),
    ([113, 234, 145, 113, 155], 113, [0, 3]),
    ([3, 8, 5, 7], 4, []),
    ([], 10, []),
    ([3, 2, 3, 4, 3], 3, [0, 2, 4])
])
def test2(numbers, target, expected):
    assert find_all_indices(numbers, target) == expected
    assert check_contains_loop(find_all_indices)

@pytest.mark.parametrize("numbers, expected", [
    ([10, 20, 30, 40, 50, 60], [20, 10, 40, 30, 60, 50]),
    ([1, 2, 3, 4, 5, 6, 7, 8], [2, 1, 4, 3, 6, 5, 8, 7]),
    ([100, 200, 300, 400], [200, 100, 400, 300]),
    ([1, 2, 3, 4, 5], [2, 1, 4, 3, 5]),
    ([100], [100]),
    ([], [])
])
def test3(numbers, expected):
    assert swap_even_odd_indices(numbers) == expected
    assert check_contains_loop(swap_even_odd_indices)
