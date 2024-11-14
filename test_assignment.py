import pytest
import inspect
from assignment import find_pair_with_sum, find_majority_element, move_zeroes_to_end

def check_contains_loop(function):
    source = inspect.getsource(function)
    return 'for' in source or 'while' in source

@pytest.mark.parametrize("numbers, target_sum, expected", [
    ([3, 8, 2, 5, 10, 7], 15, [5, 10]),
    ([2, 7, 11, 15, 4], 9, [2, 7]),
    ([1, 2, 3, 4, 5], 20, []),
    ([3, 8, 4, 7, 12, 6], 10, [3, 7]),
    ([-4, 0, 3, 1, -1, 5, -5], 0, [-5, 5])
])
def test1(numbers, target_sum, expected):
    assert find_pair_with_sum(numbers, target_sum) == expected
    assert check_contains_loop(find_pair_with_sum)

@pytest.mark.parametrize("numbers, expected", [
    ([3, 8, 3, 5, 3, 7], 3),
    ([2, 3, 2, 4, 2, 2, 5], 2),
    ([1, 1, 1, 2, 2, 2, 2], 2),
    ([1, 2, 3, 4, 5], 0),
    ([6, 6, 7, 7, 8, 8, 9, 9], 0)
])
def test2(numbers, expected):
    assert find_majority_element(numbers) == expected
    assert check_contains_loop(find_majority_element)

@pytest.mark.parametrize("numbers, expected", [
    ([0, 2, 1, 0, 5, 0, 7], [2, 1, 5, 7, 0, 0, 0]),
    ([0, 3, 0, 4, 0, 1], [3, 4, 1, 0, 0, 0]),
    ([4, 0, 2], [4, 2, 0]),
    ([0, 0, 0, 0], [0, 0, 0, 0]),
    ([1, 2, 3, 0, 0, 0], [1, 2, 3, 0, 0, 0])
])
def test3(numbers, expected):
    assert move_zeroes_to_end(numbers) == expected
    assert check_contains_loop(move_zeroes_to_end)
