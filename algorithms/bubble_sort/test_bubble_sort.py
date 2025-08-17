from .bubble_sort import bubble_sort


def test_bubble_sort():
    unsorted = [64, 34, 25, 12, 22, 11, 90]
    assert bubble_sort(unsorted) == [11, 12, 22, 25, 34, 64, 90]
