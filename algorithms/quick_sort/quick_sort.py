def quick_sort(array_):
    """
    Быстрая сортировка.

    :param array_:
    :return:
    """
    if len(array_) <= 1:
        return array_

    pivot = array_[len(array_) // 2]
    left = [x for x in array_ if x < pivot]
    middle = [x for x in array_ if x == pivot]
    right = [x for x in array_ if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)
