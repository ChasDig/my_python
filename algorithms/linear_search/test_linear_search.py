from .linear_search import linear_search


def test_linear_search():
    numbers = [4, 2, 7, 1, 9, 3]
    assert linear_search(numbers, 7) == 2
    assert linear_search(numbers, 5) is None
