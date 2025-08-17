from .quick_sort import quick_sort


def test_quick_sort():
    numbers = [3, 6, 8, 10, 1, 2, 1]
    assert quick_sort(numbers) == [1, 1, 2, 3, 6, 8, 10]
