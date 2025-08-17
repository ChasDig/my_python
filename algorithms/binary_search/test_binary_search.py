from .binary_search import binary_search


def test_binary_search():
    sorted_numbers = [1, 3, 5, 7, 9, 11]
    assert binary_search(sorted_numbers, 7) == 3
    assert binary_search(sorted_numbers, 2) is None
