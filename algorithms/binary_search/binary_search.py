def binary_search(array_, target):
    """
    Бинарный поиск в отсортированном массиве.

    :param array_:
    :param target:
    :return:
    """
    left, right = 0, len(array_) - 1

    while left <= right:
        middle = (left + right) // 2

        if array_[middle] == target:
            return middle

        elif array_[middle] > target:
            right = middle - 1

        else:
            left = middle + 1

    return None
